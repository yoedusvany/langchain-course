from dotenv import load_dotenv
import os
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages.human import HumanMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search(query: str) -> str:
    """
    Tool that searches for information on the web.

    Args:
        query (str): The search query.

    Returns:
        str: The search results.
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)


llm = ChatOllama(model="llama3.2")
tools = [search]
agent = create_agent(llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    # result = agent.invoke({"messages": HumanMessage(content="What is the capital of France?")})
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 jobs for an AI engineer using langchain in niagara region on linkedin and list the details?")})
    print(result)
   
if __name__ == "__main__":
    main()
