from langchain_groq import ChatGroq
from crewai_tools import ScrapeWebsiteTool
from dotenv import load_dotenv
from crewai import Agent
import os

def Teacher(history):
    load_dotenv()
    api_key     = os.getenv('GROQ_API_KEY')
    model_name  = os.getenv('MODEL', 'mixtral-8x7b-32768')
    default_llm = ChatGroq(groq_api_key=api_key, model=model_name)
    search_tool = ScrapeWebsiteTool()

    writer = Agent(
    role = 'Professor',
    goal = 'Escrever artigos envolventes sobre {topic}',
    tool = [search_tool],
    llm  = default_llm,
    verbose = True,
    backstory = history
    )
    return writer
