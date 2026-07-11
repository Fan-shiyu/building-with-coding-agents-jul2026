# CLAUDE.md template (Part B)

Fill in the three `✏️ TODO` spots below, then save this file as
**`CLAUDE.md` in the repo root**. Delete this header block when you save.

Remember the rule of thumb: CLAUDE.md holds what is true for **every**
session in this project. Task-specific instructions belong in your brief.

---

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

✏️ TODO 1 — Add ONE more rule of your own to the list above.
Think: what would annoy you if the agent did it without asking?
(Examples to spark ideas: deleting files, touching the solutions/ folder,
committing to git on its own.)

## Workflow
- For any task that creates more than one file: propose a plan first and
  wait for approval before writing code.

✏️ TODO 2 — Below are three candidate instructions. ONE of them belongs
in this CLAUDE.md; the other two are task-specific and belong in a brief
instead. Add the right one above and delete the other two:

  a) "Charts should use the Plotly Set2 color palette."
  b) "The trends view should use a line chart, not bars."
  c) "Add a Top-N slider to the geography view."

## About the data
✏️ TODO 3 — Write ONE sentence a new agent session should always know
about this dataset. (Hint: is there anything surprising about margins in
this data? Check the Profitability tab of the reference dashboard — or
ask your agent to check data/ and tell you.)
```

---

### Why these three blanks?

- **TODO 1** practices writing a guardrail in your own words.
- **TODO 2** practices the core sorting skill: *durable* project knowledge
  (belongs here) vs. *task* instructions (belong in the brief). Only (a)
  is true for every future session.
- **TODO 3** practices capturing domain knowledge so no future session
  starts from zero.
