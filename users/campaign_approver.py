from autogen_agentchat.agents import UserProxyAgent
import streamlit as st

def getCampaignApproverUserProxyAgent(input_func):
    campaign_Approver = UserProxyAgent(
        name='Campaign_Approver',
        input_func=input_func,
        description='You are the Campaign Approver. You give the final go-ahead for the social media posts. When the Copywriter presents the campaign.'
    )
    return campaign_Approver   
