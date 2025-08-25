import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, load_tools, AgentType

from langchain_experimental.utilities.python import PythonREPL
from langchain_core.tools import Tool
from langchain_experimental.tools.python.tool import PythonREPLTool

# Use the built-in REPL tool class
repl_tool = PythonREPLTool()


# --- Load API key from file ---
with open("openai_key.txt", "r") as f:
    os.environ["OPENAI_API_KEY"] = f.read().strip()

# --- Initialize LLM ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- Load multiple tools ---
tools = load_tools(
    ["llm-math", "wikipedia"],
    llm=llm
)

tools.append(repl_tool)

# --- Initialize Complex Agent ---
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # reasoning loop
    verbose=True
)

# --- Example Complex Query ---
query = """
Who is the current Prime Minister of India?
Take the number of letters in their first name,
multiply it by 3, then calculate the square root of that number.
"""

response = agent.run(query)
print("\nFinal Answer:", response)
