from autogen_agentchat.agents import AssistantAgent
from prompts.prompts import sys_msg_copy_writer

def getCopWriterAgent(model_client):
    copywriter_Agent = AssistantAgent(
        name='Copywriter_Agent',
        model_client=model_client,
        system_message=sys_msg_copy_writer,
        description='U are a Copy writer agent'
    )

    return copywriter_Agent

