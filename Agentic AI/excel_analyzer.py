import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI

# --- Page Config ---
st.set_page_config(page_title="AI Excel Analyzer", page_icon="📊", layout="wide")
st.title("📊 AI Excel Analyzer")
st.write("Upload an Excel file and ask AI questions about it!")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.write("### Preview of Data")
    st.dataframe(df.head())

    # --- AI Connection ---
    with open("openai_key.txt") as f:
        api_key = f.read().strip()
    llm = OpenAI(api_token=api_key)
    sdf = SmartDataframe(df, config={"llm": llm})

    # --- Chat with AI ---
    st.write("### 🔎 Ask a Question")
    query = st.text_input("Example: 'Show me average sales per region'")
    
    if query:
        with st.spinner("AI is analyzing your data..."):
            try:
                answer = sdf.chat(query)
                if isinstance(answer, str):
                    st.write("**Answer:**", answer)
                else:
                    # Sometimes PandasAI returns plots directly
                    st.pyplot(answer)
            except Exception as e:
                st.error(f"Error: {e}")
