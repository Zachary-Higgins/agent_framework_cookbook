# Copilot Instructions

Unofficial cookbook for Microsoft's `agent_framework`. Keep edits small, safe, and easy to review.

## Quick Facts
- `README.md` is the cookbook directory—update it whenever you add runnable files.
- Code samples live in `samples/`; tests live in `tests/`.
- Python tooling only; use `pytest -q` to verify logic and `python samples/opanai_basic/main.py` for a smoke check.

## Do This
- Mirror existing style and naming; change only what the request needs.
- Add tests (or update ones in `tests/`) whenever behavior changes.
- Describe your changes clearly when summarizing or committing.

## Avoid This
- Shipping secrets, tokens, or undocumented endpoints.
- Large refactors without an explicit request.
- Leaving failing tests—run them and mention the result.

## Standard Workflow
1. Understand the ask and note the files you will touch.
2. Plan briefly (todo list), then make the minimal edits.
3. Run `pytest -q`; if you add a runnable example, note how to execute it.
4. Summarize what changed and call out any follow-up work.

## Typical Responses
- Feature request → add targeted code + tests + short summary.
- Failing test → reproduce with `pytest -q`, fix root cause, rerun.
- Docs ask → edit Markdown, add concise command snippets if useful.

This repo is personal and not affiliated with Microsoft; for upstream issues, refer to the official `agent_framework` project.
