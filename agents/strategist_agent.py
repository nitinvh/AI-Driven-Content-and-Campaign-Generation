from autogen_agentchat.agents import AssistantAgent
from prompts.prompts import sys_msg_stratergy

def getStrategistAgent(model_client):
    strategist_Agent = AssistantAgent(
        name='Strategist_Agent',
        model_client=model_client,
        system_message=sys_msg_stratergy,
        description='u are a strategist agent'
    )

    return strategist_Agent

