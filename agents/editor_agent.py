from autogen_agentchat.agents import AssistantAgent
from prompts.prompts import sys_msg_editor

def getEditorAgent(model_client):
    editor_agent = AssistantAgent(
    name="Editor_Agent",
    model_client=model_client,
    description="U are a editor agent",
    system_message=sys_msg_editor,
    )

    return editor_agent

