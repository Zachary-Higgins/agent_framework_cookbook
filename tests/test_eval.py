import base64
import dotenv
import json
import os
import subprocess
import sys

dotenv.load_dotenv()

abs_path = os.path.dirname(__file__)
abs_eval_path = os.path.join(abs_path, "evaluator", "main.py")
    
    
def run_test_agent(agents_path):
    abs_agent_path = os.path.join(abs_path, agents_path)
    cmd_agent = [sys.executable, abs_agent_path, "--test"]
    agent_stdout = subprocess.run(cmd_agent, capture_output=True, text=True).stdout
    return agent_stdout.encode("utf-8")

def run_eval_test(agents_path):
    agent_stdout = run_test_agent(agents_path)
    
    # Evaluate Inference
    base64_input = base64.b64encode(agent_stdout).decode("utf-8")
    cmd_eval = [sys.executable, abs_eval_path, "--base64_input", base64_input]
    eval_stdout = subprocess.run(cmd_eval, capture_output=True, text=True).stdout
    
    # Validate Result
    result = json.loads(eval_stdout.encode("utf-8"))
    assert result['clarity'] == True, "Clarity evaluation failed."
    assert result['relevance'] == True, "Relevance evaluation failed."
    assert result['helpfulness'] == True, "Helpfulness evaluation failed."    


# Basic Execution Tests
def test_run_personas_agent():
    path = os.path.join("openai_personas","main.py")
    result = run_test_agent(path)
    assert len(result) > 1, "Result is empty."
    
def test_run_tools_agent():
    path = os.path.join("openai_tools","main.py")
    result = run_test_agent(path)
    assert len(result) > 1, "Result is empty."


# Evaluation Tests
def test_eval_personas_agent():
    path = os.path.join("openai_personas","main.py")
    _ = run_eval_test(path)
    
def test_eval_tools_agent():
    path = os.path.join("openai_tools","main.py")
    _ = run_eval_test(path)