from autogen_agentchat.agents import UserProxyAgent

def getContentReviewerUserProxyAgent(input_func):
    content_reviewer = UserProxyAgent(
        name='Content_Reviewer',
        input_func=input_func,
        description='You are the Content Reviewer. Your role is to give the final verdict on the article. When the Editor presents the final draft.',
    )
    return content_reviewer   
