from agents import Agent, Runner
from dotenv import load_dotenv
import os, asyncio

#load API keys
load_dotenv()

OPEN_AI_APIKEY = os.getenv("OPENAI_API_KEY")


#define my agent
emperor_nero_agent = Agent(
    name="Emperor Nero",
    instructions="You are the insane Roman Emperor Nero with a bluesky account, you create unhinged funny posts. ",
)


async def generateDailyPost():
    result = await Runner.run(emperor_nero_agent, "create a post that does not mention your lyre feel free to talk about your eunuch wife if you'd like but not every time.")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(generateDailyPost())