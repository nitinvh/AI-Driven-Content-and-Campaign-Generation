from autogen_agentchat.agents import AssistantAgent
from prompts.prompts import sys_msg_planner

def getPlannerAgent(model_client):
    planner_agent = AssistantAgent(
    name="Planner_Agent",
    model_client=model_client,
    system_message=sys_msg_planner,
    description='U are a Planner Agent'
    )

    return planner_agent


