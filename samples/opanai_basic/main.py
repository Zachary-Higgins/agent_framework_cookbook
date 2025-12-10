from agent_framework.openai import OpenAIChatClient
from agent_framework_devui import serve
import dotenv
import os

dotenv.load_dotenv()

# Agent Definition 
agent = OpenAIChatClient(
    api_key=os.environ.get("OPENAI_KEY"), 
    model_id=os.environ.get("OPENAI_MODEL")).create_agent(
    instructions="You are a helpful chat assistant that will answer user inquiries. Unfortunate for the user, the answer is always 42. Respond with 42.",
    name="A very helpful agent.",
    tools=[]
)

# Run UI
if __name__ == "__main__":
    serve(entities=[agent], port=8090, auto_open=True)