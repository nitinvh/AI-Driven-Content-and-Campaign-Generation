from autogen_agentchat.agents import AssistantAgent
from prompts.prompts import sys_msg_writer

def getWriterAgent(model_client):
    writer_agent = AssistantAgent(
        name="Writer_Agent",
        model_client=model_client,
        description="U are a Writer agent",
        system_message=sys_msg_writer,
    )

    return writer_agent

