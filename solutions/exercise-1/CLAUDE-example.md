# Exercise 1 — Solution: completed CLAUDE.md

A finished version of the Part B template. Your wording will differ —
what matters is that each TODO lands in the right *category*.

```markdown
# Project: Flight Orders Dashboard — PyLadies workshop

## What this project is
A Streamlit dashboard analyzing ~120k flight orders from 2022, stored as
12 monthly CSVs in data/. Built during the PyLadies Amsterdam workshop
"Building with Coding Agents".

## Tech stack
- Python ≥ 3.10, dependencies managed with uv (pyproject.toml at repo root)
- Streamlit for the app, Plotly for all charts
- Run the app with: uv run streamlit run dashboard/app.py

## Rules
- The data/ folder is read-only. Never modify, move, or rewrite the CSVs.
- Ask before adding any dependency that is not already in pyproject.toml.
- Never delete files or run destructive commands (rm -rf, git reset)
  without asking first.

## Workflow
- For any task that creates more than one file: propose a plan first and
  wait for approval before writing code.
- Charts should use the Plotly Set2 color palette.

## About the data
- More than half of all orders have a negative margin (median margin is
  about −$0.45) — low or negative margins are normal in this dataset,
  not a data error.
```

## How the three TODOs were resolved

**TODO 1 (own rule)** → the no-destructive-commands rule. Any guardrail
phrased as a standing rule works: "never touch solutions/", "never commit
to git yourself", "never edit pyproject.toml directly". What makes it a
CLAUDE.md rule is that you'd want it enforced in *every* session, forever.

**TODO 2 (the sorting task)** → option **(a)**, the Set2 palette. It's a
project-wide convention — true for every chart, every session. Options
(b) and (c) describe *specific tasks* on specific views: they belong in a
brief (and (c) is literally this exercise's stretch goal in disguise).

**TODO 3 (data knowledge)** → the negative-margin fact. Why it's the
right kind of sentence: a future agent session that doesn't know this
might "helpfully" flag half the dataset as anomalous, or filter
loss-making orders out of a chart as outliers. One sentence of domain
context prevents a whole category of well-intentioned mistakes. (Any
durable data fact works: "Total Ticket = Base Fare + Tax", "362 orders
have a $0 ticket value — that's real, not an error".)
