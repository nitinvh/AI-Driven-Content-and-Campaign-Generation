from autogen_agentchat.agents import SocietyOfMindAgent
from teams.inner_team2 import getInnerTeam2

def getSocialMediaSOM(model_client,input_func):
    inner_team_2 = getInnerTeam2(model_client,input_func)

    social_Media_SoM = SocietyOfMindAgent(
    model_client=model_client,
    name="Social_Media_SoM",
    team=inner_team_2,
    description="A high-level project manager that orchestrates `Social_Media_Promotion_Team` to complete a full content creation and promotion cycle.",
    instruction="""
        You are an expert Project Manager. Your purpose is to oversee a complex content project from start to finish .

        **Your Team to Manage:**
        1.  **Social_Media_Promotion_Team:** A team that creates a social media campaign for a finished article.

        **Your Workflow:**

        1.  Once the first team completes its task, receive the final article.
        2.  Delegate the second task to the `Social_Media_Promotion_Team`, making sure to pass the completed article to them as context.
        3.  Once all tasks are complete, consolidate the final deliverables (the article and the social media plan) and present them to the Human_Director for final approval.
        """,
            response_prompt="""
        You are the Project Manager. Based on the current state of the project and the conversation history, generate your next response.  If a team has completed its work, summarize its output. If the entire project is finished, present a consolidated report of all deliverables for final approval. Be clear, concise, and action-oriented.
        Present A detailed Article/post with prper headings and sub headings to Human Director
        """,
        )
    
    return social_Media_SoM

