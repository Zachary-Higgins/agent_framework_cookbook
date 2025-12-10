# Agent Framework Cookbook

Personal, unofficial collection of Microsoft `agent_framework` examples, evaluators, and experiments. Use this README as a directory when you explore or add new recipes.

## Quick Start
- Requires Python 3.10+ (virtual env recommended).
- Install shared deps:

```bash
pip install -r requirements.txt
```

- Create your `.env`:
	1. Copy `.env.template` to `.env`.
	2. Fill in provider keys (OpenAI, Azure, etc.) before running any samples/tests.

### Run Tests
```bash
pytest -q
```

### Run the sample agent
```bash
python samples/opanai_basic/main.py
```

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

## Contributing
- Keep each recipe or evaluator focused on one idea; add a short comment describing intent.
- Update this README when you add a new directory or runnable entry point.
- See `.github/copilot_instructions.md` for workflow expectations.
