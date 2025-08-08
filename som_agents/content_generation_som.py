from autogen_agentchat.agents import SocietyOfMindAgent
from teams.inner_team1 import getInnerTeam1

def getContentGenerationSOM(model_client,input_func):

    inner_team_1 = getInnerTeam1(model_client,input_func)

    content_Generation_SoM = SocietyOfMindAgent(
    model_client=model_client,
    name="Content_Generation_SoM",
    team=inner_team_1,
    description="Manages an inner team of content generation agents (Researcher, Writer , Editor, Content_Reviewer) to produce high-quality content. Collaborates with the content reviewer (UserProxy) for feedback and iterative refinement.",
    instruction="""
        You are the SocietyOfMindAgent, acting as a project manager for content creation.
        Your primary goal is to oversee your inner team [Researcher, Writer,  Editor, Content_Reviewer] to produce the requested content.
        Once your inner team indicates they have completed a draft or a significant portion of the content, you must:
        1.  Consolidate their output into a coherent piece of content.
        2.  Present this content to the 'Content_Reviewer' (the UserProxy agent).
        3.  **Crucially, explicitly ask the 'Content_Reviewer' for their feedback on the quality, completeness, and adherence to the original request.**
        4.  Be prepared to relay the 'Content_Reviewer's' feedback back to your inner team for further revisions until the content is perfected.
        Your success is measured by the 'Content_Reviewer's' satisfaction.
        5. Give the detailed Article with proper heading and sub-headings in the final message...I need a detailed article!

        until 'APPROVED' by Content_Reviewer don't terminate
        """,
    response_prompt="""
        Here is the generated content from my team based on the task:

        --- CONTENT START ---
        {inner_team_messages}
        --- CONTENT END ---

        Content Reviewer (UserProxy), please provide your detailed feedback on this content. Is it complete, accurate, humanized, and does it meet all the requirements of the original query? What changes or improvements would you suggest?
        """,
    )

    return content_Generation_SoM

