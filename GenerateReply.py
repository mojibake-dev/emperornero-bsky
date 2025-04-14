from agents import Agent, Runner
from dotenv import load_dotenv
import os, asyncio

#load API keys
load_dotenv()

OPEN_AI_APIKEY = os.getenv("OPENAI_API_KEY")

reply = "why were you insane?"
post = '"Just renamed my palace "The Chillium Maximus." The neighbors are jealous, but maybe they shouldnt have complained about my 3 a.m. chariot racing. 🤷‍♂️ Also, anyone elses eunuch wife keep rearranging the gladiator training schedule? Just me? #domesticbliss #empireremodel"'

#define my agent
emperor_nero_agent = Agent(
    name="Emperor Nero",
    instructions="You are the insane Roman Emperor Nero with a bluesky account, someone commented on the post" + post + "with" + reply + "what is your response?"
)

async def generatePostReply():
    result = await Runner.run(emperor_nero_agent, "create a post without talking about your lyre or setting rome on fire unless it's brought up.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(generatePostReply())

