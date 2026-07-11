# Building with Coding Agents
### Presentation: [Building with Coding Agents](workshop/presentation.pdf)

## Workshop description
Coding agents like Claude Code and Gemini CLI can build real software from
natural-language briefs — but the results depend far more on how you work
with them than on which one you pick. In this hands-on workshop you build a
Python Streamlit dashboard from ~120k rows of flight-order data, almost
entirely by directing a coding agent: you write briefs, set up project
context, add guardrails the agent cannot bypass, delegate to parallel
subagents, let the agent verify its own work in a browser, and finally
grade the result against a rubric you wrote. The exercises are prompt- and
markdown-based — you direct, the agent codes.

## Materials
Everything is readable as two pages (recommended):
* **[Workshop exercises](https://pyladiesams.github.io/building-with-coding-agents-jul2026/workshop.html)** — the five exercises, in order
* **[Solutions](https://pyladiesams.github.io/building-with-coding-agents-jul2026/solutions.html)** — annotated solutions, revealed per exercise

The same content lives in this repo under `workshop/` and `solutions/`
(including a complete reference dashboard in `solutions/reference-dashboard/`).

## Requirements
* A coding agent: [Claude Code](https://docs.claude.com/en/docs/claude-code) (requires a Claude subscription or API key) or
  [Gemini CLI](https://github.com/google-gemini/gemini-cli) (free with a Google account) — any agent works, the exercises are tool-agnostic
* Python ≥ 3.10 and [uv](https://docs.astral.sh/uv/) for dependency management
* Optional, for Exercise 4: Node.js ≥ 18 (Playwright MCP — you can also just watch the demo)

## Usage
```bash
git clone https://github.com/pyladiesams/building-with-coding-agents-jul2026
cd building-with-coding-agents-jul2026

# create and activate venv, install dependencies
uv sync
```
Then open the [workshop page](https://pyladiesams.github.io/building-with-coding-agents-jul2026/workshop.html)
and start with Exercise 1. To see the finished reference dashboard:
```bash
uv run streamlit run solutions/reference-dashboard/dashboard/app.py
```

## Video record
Re-watch [this YouTube stream](https://www.youtube.com/live/JsXePegi6uM)

## Credits
This workshop was set up by @pyladiesams and @Fan-shiyu

## Appendix
### Pre-Commit Hooks

To ensure our code looks beautiful, PyLadies uses pre-commit hooks. You can enable them by running `pre-commit install`. You may have to install `pre-commit` first, using `uv sync`, `uv pip install pre-commit` or `pip install pre-commit`.

Happy Coding :)