import os
import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

# --- Load API key from file ---
with open("openai_key.txt") as f:
    os.environ["OPENAI_API_KEY"] = f.read().strip()

# --- Streamlit UI ---
st.set_page_config(page_title="Codebase Q&A", layout="wide")
st.title("💻 Codebase Q&A Agent")

# Sidebar: Upload / select code folder
code_dir = st.text_input("📂 Path to codebase", "my_project")

if "qa" not in st.session_state:
    st.session_state.qa = None

# Build index button
if st.button("🔍 Build Index"):
    st.write("Loading codebase...")

    # Load files
    docs = []
    for root, _, files in os.walk(code_dir):
        for fname in files:
            if fname.endswith(".py") or fname.endswith(".csv"):
                path = os.path.join(root, fname)
                with open(path, "r", errors="ignore") as f:
                    docs.append(f.read())

    # Split
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.create_documents(docs)

    # Embeddings + FAISS
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    db = FAISS.from_documents(chunks, embeddings)

    # Save to reuse
    db.save_local("codebase_index")

    retriever = db.as_retriever(search_kwargs={"k": 4})
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    st.session_state.qa = RetrievalQA.from_chain_type(
        llm=llm, retriever=retriever, chain_type="stuff"
    )

    st.success("✅ Index built and ready!")

# Query box
if st.session_state.qa:
    query = st.text_input("❓ Ask a question about the codebase")
    if query:
        with st.spinner("Thinking..."):
            answer = st.session_state.qa.run(query)
        st.markdown("### 🧠 Answer")
        st.write(answer)
