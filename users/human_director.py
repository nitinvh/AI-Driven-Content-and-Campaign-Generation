from autogen_agentchat.agents import UserProxyAgent

def getHumanDirectorUserProxyAgent(input_func):
    human_director = UserProxyAgent(
        name='Human_Director',
        input_func=input_func,
        description='U are a Human Director, review and approve the content'
    )
    return human_director   
