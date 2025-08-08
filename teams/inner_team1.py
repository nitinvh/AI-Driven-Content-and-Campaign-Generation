from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

from agents.researcher_agent import getResearcherAgent
from agents.writer_agent import getWriterAgent
from agents.editor_agent import getEditorAgent
from users.content_reviewer import getContentReviewerUserProxyAgent

def getInnerTeam1(model_client, input_func):

    researcher_agent = getResearcherAgent(model_client)
    writer_agent = getWriterAgent(model_client)
    editor_agent= getEditorAgent(model_client)
    content_reviewer = getContentReviewerUserProxyAgent(input_func)

    inner_team_1 = RoundRobinGroupChat(
        participants=[researcher_agent,writer_agent,editor_agent,content_reviewer],
        termination_condition=TextMentionTermination('APPROVED'),
        max_turns=20,
        description="Ask Content_Reviewer for feedback"
    )

    return inner_team_1

