import streamlit as st
import asyncio
import os

from teams.selector_team import getSelectorTeam
from models.gemini_model_client import get_model_client
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage

st.title('AI Driven Content and Campaign Generation Tool')

task = st.chat_input("Enter ur task here")

async def run_tool(team):
    try:
        async for message in team.run_stream(task=task):
            print(message)
            if isinstance(message,TextMessage):
                if message.source.startswith('user'):
                    with st.chat_message('user',avatar='👤'):
                        st.markdown(message.content)
                elif message.source.startswith('Content_Reviewer'):
                    with st.chat_message('Data_Analyzer_agent',avatar='👤'):
                        st.markdown(message.content)
                elif message.source.startswith('Campaign_Approver'):
                    with st.chat_message('Campaign_Approver',avatar='👤'):
                        st.markdown(message.content)
                elif message.source.startswith('Human_Director'):
                    with st.chat_message('Human_Director',avatar='👤'):
                        st.markdown(message.content)
                else:
                    with st.chat_message(message.source,avatar='🤖'):
                        st.markdown(message.content)
               
            
            elif isinstance(message,TaskResult):
                st.markdown(f"Stop reason : {message.stop_reason}")
        return None
    except Exception as e:
        st.error(f"Error:{e}")
        return e

if task:
    try:
        model_client = get_model_client()
        team = getSelectorTeam(model_client,st.text_input('provide feedback'))

        error = asyncio.run(run_tool(team))
        if error:
            st.error(f"An error occured:{error}")
    
    except Exception as e:
        st.error(f"Error:{e}")

else:
    st.warning('Please provide the task')

        
