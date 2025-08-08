import os
from dotenv import load_dotenv
load_dotenv()

TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")

from langchain_community.tools import TavilySearchResults

web_crawler = TavilySearchResults(tavily_api_key= TAVILY_API_KEY)

def web_crawler_func(query:str):
    '''It searches with the given query'''
    result = web_crawler.invoke(query)
    return result


