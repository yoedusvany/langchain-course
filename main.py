from dotenv import load_dotenv
import os
load_dotenv()

from langchain.agents import create_agent
from langchain_core.messages.human import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch


llm = ChatOllama(model="llama3.2")
tools = [TavilySearch()]
agent = create_agent(llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    # result = agent.invoke({"messages": HumanMessage(content="What is the capital of France?")})
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 jobs for an AI engineer using langchain in niagara region on linkedin and list the details?")})
    print(result)
   
if __name__ == "__main__":
    main()
