# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Python 3.13 project exploring a LangChain financial-advice agent powered by OpenRouter-hosted models. Early scaffold — single-file `main.py` entry point.

## Tooling

Dependencies are managed with **uv** (lockfile is `uv.lock`, not `requirements.txt`).

```bash
uv sync                    # Install/update dependencies from uv.lock
uv run python main.py      # Run the agent
uv add <package>           # Add a dependency (updates pyproject.toml + uv.lock)
```

Do not edit `uv.lock` by hand; let `uv` regenerate it.

## Runtime configuration

`main.py` calls `load_dotenv()`, so secrets are read from `.env` in the project root (gitignored). An `OPENROUTER_API_KEY` is required for `langchain-openrouter` to authenticate. The model is hardcoded in `main.py` via the `FINANCIAL_MODEL` constant using the `openrouter:<provider>/<model>` URI scheme consumed by `langchain.agents.create_agent`.

## Architecture

The agent is built with LangChain 1.x's `create_agent` API (not the legacy `AgentExecutor`/`initialize_agent` pattern). Messages flow as `HumanMessage` objects inside a `{"messages": [...]}` dict; the response is the same shape, and the final assistant reply is `result["messages"][-1].content`. Keep new code aligned with this message-list convention rather than reverting to the older prompt-template style.
