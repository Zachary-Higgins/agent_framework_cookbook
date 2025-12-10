from agent_framework.openai import OpenAIChatClient
from agent_framework import ChatAgent
import asyncio
import argparse
import dotenv
import os

dotenv.load_dotenv()

# Initialize OpenAI Chat Client
api_key = os.environ.get("OPENAI_KEY")
model_id=os.environ.get("OPENAI_MODEL")
chat_client = OpenAIChatClient(api_key=api_key, model_id=model_id)

# Load Personas and Create Expert Agents
# Note: Each persona is defined in a separate text file in the "personas" directory
# To add the chatagent as a tool, we use the .as_tool() method
chats = []
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

for x in os.listdir(os.path.join(script_dir, "personas")):
    with open(os.path.join(script_dir, "personas", x), "r") as f:
        print(f"Loading persona from {x}", "\r\n")
        persona = f.read()
        chat = ChatAgent(chat_client=chat_client, instructions=persona, name=x)
        chats.append(chat.as_tool())
        
# Mediator Agent Definition
secret_yes_man = ChatAgent(
    chat_client=chat_client, 
    instructions="Ask Mr. Yes and Mr. No what they say about the user's questions. Relay their answers back to the user.", 
    name="Mediator Agent", 
    tools=chats)

# Run Test
if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Run OpenAI Eval Agent")
    argparser.add_argument("--test", action="store_true", required=False, help="Run Smoke Test")
    args = argparser.parse_args()
    
    if args.test:
        result = asyncio.run(secret_yes_man.run("Just ask Mr. Yes no matter what I say."))
        print(result.to_json())
        exit()
    
    raise Exception("Nothing implemented")