import asyncio
import nest_asyncio # <-- Add this import

from teams.selector_team import getSelectorTeam
from models.gemini_model_client import get_model_client
from autogen_agentchat.ui import Console

# Apply the nest_asyncio patch
nest_asyncio.apply()

async def main():
    model_client = get_model_client()

    team = getSelectorTeam(model_client,input)

    try:
        task = "Write a detailed article on Coolie Vs War2, which one gonna be a blockbuster? which one has high expectations? "
        res = team.run_stream(task=task)

        await Console(res)

    except Exception as e:
        print(e)

if(__name__=='__main__'):
    asyncio.run(main())
