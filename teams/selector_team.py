from autogen_agentchat.teams import SelectorGroupChat
from agents.planner_agent import getPlannerAgent
from som_agents.content_generation_som import getContentGenerationSOM
from som_agents.social_media_som import getSocialMediaSOM
from users.human_director import getHumanDirectorUserProxyAgent
from prompts.prompts import selector_prompt
from autogen_agentchat.conditions import TextMentionTermination



def getSelectorTeam(model_client,input_func):
    planner_agent = getPlannerAgent(model_client)
    content_Generation_SoM = getContentGenerationSOM(model_client,input_func)
    social_Media_SoM = getSocialMediaSOM(model_client,input_func) 
    human_director = getHumanDirectorUserProxyAgent(input_func)

    selector_team = SelectorGroupChat(
        participants=[planner_agent,content_Generation_SoM,social_Media_SoM,human_director],
        model_client=model_client,
        termination_condition=TextMentionTermination("FINALIZE"),
        max_turns=12,
        selector_prompt=selector_prompt,
        allow_repeated_speaker=True
    )

    return selector_team

