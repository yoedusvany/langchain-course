from typing import List
from pydantic import BaseModel, Field
import os
import warnings
from dotenv import load_dotenv
warnings.filterwarnings("ignore", category=UserWarning, module="langchain_tavily")

load_dotenv()

from langchain.agents import create_agent
from langchain_core.messages.human import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Schema for a source  used in the agent"""
    name: str = Field(description="Name of the source")
    url: str = Field(description="URL of the source")

class AgentResponse(BaseModel):
    """Schema for the agent response"""
    answer: str = Field(description="Answer to the question")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to answer the question")    


llm = ChatOllama(model="llama3.2")
tools = [TavilySearch()]
agent = create_agent(llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="Search for 3 jobs for an AI engineer using langchain in niagara region on linkedin and list the details?")]})
    
    print("\n--- AGENT RESULT KEYS ---")
    print(result.keys())
    
    if "response" in result:
        print("\n--- STRUCTURED RESPONSE ---")
        print(result["response"])
    else:
        print("\n--- NO STRUCTURED RESPONSE FOUND ---")
        # El último mensaje podría tener la respuesta si el agente no la movió a una clave aparte
        print("Last message content:", result["messages"][-1].content)
   
if __name__ == "__main__":
    main()
