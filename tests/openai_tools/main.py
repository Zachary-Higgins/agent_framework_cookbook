from agent_framework.openai import OpenAIChatClient
from agent_framework import ChatAgent
from tools.demo_tools import demo_tools
import argparse
import dotenv
import os
import asyncio

dotenv.load_dotenv()

# Initialize OpenAI Chat Client
api_key = os.environ.get("OPENAI_KEY")
model_id=os.environ.get("OPENAI_MODEL")
chat_client = OpenAIChatClient(api_key=api_key, model_id=model_id)

# Tools / Expert Agents
tools = [demo_tools.another_demo_tool, demo_tools.demo_tools_function]
        
# Mediator Agent Definition
demo_agent = ChatAgent(
    chat_client=chat_client, 
    instructions="You are a demo mediator agent that uses demo tools to assist users. Use the provided tools to answer user queries effectively.", 
    name="Demo Mediator Agent", 
    tools=tools)

# Run Test
if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Run OpenAI Eval Agent")
    argparser.add_argument("--test", action="store_true", required=False, help="Run Smoke Test")
    args = argparser.parse_args()
    
    if args.test:
        result = asyncio.run(demo_agent.run("Help me with a demo task. My input is 42."))
        print(result.to_json())
        exit()
    
    raise Exception("Nothing implemented")