from autogen_agentchat.agents import AssistantAgent
from autogen_core.tools import FunctionTool
from prompts.prompts import sys_msg_researcher

from tools.tavily_tool import web_crawler_func
from tools.wikipedia_tool import wikiLoader


def getResearcherAgent(model_client):
    web_crawler_tool = FunctionTool(web_crawler_func, description='Browse for up to date context')
    wiki_search_tool = FunctionTool(wikiLoader, description='Search any topic in wikipedia to write blogs')

    researcher_agent = AssistantAgent(
        name="Researcher_Agent",
        model_client=model_client,
        description="U are a Researcher, u use web_crawler_tool and wiki_search_tool to research on given topic",
        system_message=sys_msg_researcher,
        tools=[web_crawler_tool,wiki_search_tool],
        reflect_on_tool_use=True
        )
    return researcher_agent
