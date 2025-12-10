[![Manual Pytest](https://github.com/Zachary-Higgins/agent_framework_cookbook/actions/workflows/manual-pytest.yml/badge.svg)](https://github.com/Zachary-Higgins/agent_framework_cookbook/actions/workflows/manual-pytest.yml)

# Agent Framework Cookbook

Personal, unofficial collection of Microsoft `agent_framework` examples, evaluators, and experiments. Use this README as the directory of recipes.


## Quick Start
1. **Python 3.10+** – create/activate a virtual environment.
2. **Bootstrap env vars** – copy `.env.template` → `.env` and fill the required keys listed below.
3. **Install dependencies**

	```bash
	pip install -r requirements.txt
	```

4. **Run tests or samples**

	```bash
	pytest -q
	python samples/opanai_basic/main.py
	```

## Environment Variables (local + CI)
`pytest` and the manual GitHub Actions workflow (`.github/workflows/manual-pytest.yml`) share the same configuration. Define these keys in your local `.env` and mirror them as GitHub Action Secrets/Variables (`Settings → Secrets and variables → Actions`).

| Scope | Name | Example | Purpose |
| --- | --- | --- | --- |
| Secret | `OPENAI_KEY` | `OPENAI_KEY=sk-...` | Authenticates requests to the OpenAI API (tests & samples will fail without this).
| Variable | `OPENAI_MODEL` | `OPENAI_MODEL=gpt-5-nano` | Model identifier used by evaluator/samples; tweak as needed.
| Variable (optional) | `ENABLE_OTEL` | `ENABLE_OTEL=false` | Toggle tracing; defaults to `false` for local pytest runs.

**GitHub Actions:** after secrets/variables are set, trigger **Manual Pytest** in the Actions tab to run `pip install -r requirements.txt` followed by `pytest -vv` on Ubuntu.

**Local runs:** ensure the same variables exist in `.env`; `pytest` will load them via your preferred env loader (e.g., `python-dotenv`).

## Directory Guide

### Root
- `README.md` – you are here; directory of recipes and utilities.
- `.github/copilot_instructions.md` – norms for Copilot/human contributors.
- `.env.template` – seed for local secrets; copy to `.env` and fill values when required.

### `samples/`
Single-file demos meant to stay tiny and focused.

| Path | Purpose | Try it |
| --- | --- | --- |
| `samples/opanai_basic/main.py` | Minimal OpenAI-powered agent showing request/response wiring. | `python samples/opanai_basic/main.py` |

### `tests/`
Holds evaluation harnesses and regression tests for the cookbook entries.

| Path | Purpose | Notes |
| --- | --- | --- |
| `tests/test_eval.py` | Main pytest entry that wires evaluators to recipes. | Run with `pytest -q`. |
| `tests/evaluator/main.py` | Shared evaluator logic for test harnesses. | Imported by `test_eval.py`. |
| `tests/openai_personas/` | Persona-based evaluation scripts and prompt variants. | `personas/no.md` & `personas/yes.md` hold prompt text. |
| `tests/openai_tools/` | Tool-enabled agent evaluation. | `tools/demo_tools.py` registers sample tools. |

## Useful Links
Some useful links outside of this repository.
| Title | Notes | Link | 
| ----- | ---- | ----- |
| Official GitHub | Official agent_framework github (has more samples) | [https://github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework) | 
| KB - Agents As Functions | Because I had a hard time finding this the first time. | [https://learn.microsoft.com/en-us/agent-framework/tutorials/agents/agent-as-function-tool?pivots=programming-language-python](https://learn.microsoft.com/en-us/agent-framework/tutorials/agents/agent-as-function-tool?pivots=programming-language-python) |

## Contributing
- Keep each recipe or evaluator focused on one idea; add a short comment describing intent.
- Update this README when you add a new directory or runnable entry point.
- See `.github/copilot_instructions.md` for workflow expectations.
