from agent_framework.openai import OpenAIChatClient
from agent_framework import ChatAgent
from pydantic import BaseModel
import argparse
import asyncio
import dotenv
import base64
import os

dotenv.load_dotenv()

class EvalCriteria(BaseModel):
   clarity: bool
   relevance: bool
   helpfulness: bool

# Initialize OpenAI Chat Client
api_key = os.environ.get("OPENAI_KEY")
model_id=os.environ.get("OPENAI_MODEL")
chat_client = OpenAIChatClient(api_key=api_key, model_id=model_id)
        
# Eval Agent Definition
eval_agent = ChatAgent(
   chat_client=chat_client, 
   instructions="You are an evaluation agent. Your role is to assess the performance of other agents based on user feedback and predefined criteria.", 
   name="Eval Agent",
   )


if __name__ == "__main__":
   argparser = argparse.ArgumentParser(description="Run OpenAI Eval Agent")
   argparser.add_argument("--prompt", type=str, required=False, help="User prompt for evaluation")
   argparser.add_argument("--base64_input", type=str, required=False, help="Base 64 input.")
   args = argparser.parse_args()
   
   if args.base64_input:
      inputs = base64.b64decode(args.base64_input).decode("utf-8")
   else:
      inputs = args.prompt

   assert inputs is not None, "An input must be specified."
   
   result = asyncio.run(eval_agent.run(
      f"Evaluate the following agent interaction based on clarity, relevance, and helpfulness: {inputs}", 
      response_format=EvalCriteria))
   
   result_as_json = result.value.model_dump_json(indent=2)
   print(result_as_json)