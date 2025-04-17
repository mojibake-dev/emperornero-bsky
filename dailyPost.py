#Tools
import os, asyncio
from dotenv import load_dotenv
#APIs
from atproto import Client
from agents import Agent, Runner

# Load environment variables
load_dotenv()


# Bluesky credentials
BLUESKY_USERNAME = os.getenv("BLUESKY_USERNAME")
BLUESKY_PASSWORD = os.getenv("BLUESKY_PASSWORD")


async def generatePost():
    #define agent
    emperor_nero_agent = Agent(
    name="Emperor Nero",
    instructions="You are the insane Roman Emperor Nero with a bluesky account, you create unhinged funny posts. ",
    )
    print("-- Running async function to generate text post...")
    result = await Runner.run(emperor_nero_agent, "create a post that does not mention your lyre feel free to talk about your eunuch wife, sporus, but not every time.")    
    print(result.final_output)
    return result.final_output


def makePost(postText):
    # Create a Bluesky client
    client = Client("https://bsky.social")

    #connect and post
    print("-- Logging into bsky...")
    client.login(BLUESKY_USERNAME, BLUESKY_PASSWORD)
    print("-- Posting text ...")
    client.post(postText)


def main():
    postText = asyncio.run(generatePost())
    makePost(postText)

if __name__ == "__main__":
    main()

