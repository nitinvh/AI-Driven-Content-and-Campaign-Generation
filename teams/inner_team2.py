from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

from agents.strategist_agent import getStrategistAgent
from agents.copy_writer_agent import getCopWriterAgent
from users.campaign_approver import getCampaignApproverUserProxyAgent

def getInnerTeam2(model_client, input_func):
    strategist_Agent = getStrategistAgent(model_client)
    copywriter_Agent = getCopWriterAgent(model_client)
    campaign_Approver = getCampaignApproverUserProxyAgent(input_func)

    inner_team_2 = RoundRobinGroupChat(
        participants=[strategist_Agent,copywriter_Agent,campaign_Approver],
        termination_condition=TextMentionTermination("APPROVED"),
        max_turns=15
    )

    return inner_team_2

