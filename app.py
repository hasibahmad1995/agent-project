import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
model = "qwen/qwen3.8-27b"
llm = ChatGroq(model = model)

# query = "Hello, how are you?"
# response = llm.invoke(query)
# print(response.content)

from langchain.agents import create_agent
from langchain_community.utilities import GoogleSerperAPIWrapper

search = GoogleSerperAPIWrapper()
from langchain_core.tools import Tool

tools = [
    Tool(
        name="google_search",
        func=search.run,
        description="Search Google for information when you feel it is necessary. Input is a search query string.",
    )
]

sys_prompt = """You are a helpful assistant that answers questions using the Google Search API.
You should only use the Google Search API to answer questions. If you don't know the answer, you should say "I don't know" and not make up an answer.
You should also provide the source of your answer in the format: "Source: <source>"""

agent = create_agent(
    model=llm, 
    tools=tools,
    system_prompt=sys_prompt
)

while True:

    query = input("Enter your query: ")
    if query.lower() in ["exit", "quit"]:
        break
    response = agent.invoke(
        {"messages": [{"role": "user", "content": query}]}
    )
    print(response["messages"][-1].content)