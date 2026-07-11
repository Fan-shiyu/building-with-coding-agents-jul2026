# Exercise 1 — The Brief & the Plan

⚡ **Start here:** open `starter-prompt.md` first — this README walks you
through the rest, one file per step.

You are the architect. The agent is the contractor. In this exercise you'll
experience the difference between a vague request and a real brief — and
you'll never prompt the same way again.

---

## 🎯 Goal

Turn a vague prompt into a well-structured brief, set up your project's
`CLAUDE.md`, and get your agent to propose a plan you approve **before** it
writes any code. By the end, your agent is building dashboard v1 while you
move on to the next block.

## 🧠 Concepts you'll use

- **Project context (CLAUDE.md)** — the standing instructions your agent
  reads every session
- **Plan before code** — review the drawings before construction starts
- **Guardrails (soft)** — rules you state so the agent stays in bounds
- **The subcontractor mindset** — brief quality determines output quality

## 📦 What's in this folder

| File | What it is |
|---|---|
| `README.md` | This file — your instructions |
| `starter-prompt.md` | A deliberately mediocre prompt (Part A) |
| `requirements-card.md` | The project spec to build your brief from (Part C) |
| `CLAUDE-template.md` | A CLAUDE.md with blanks for you to fill (Part B) |

---

## Part A — Feel the problem

1. Open `starter-prompt.md` and copy the **bad prompt**, including the
   plan-only line at the end.
2. Paste it into your coding agent and send.
3. Read the plan that comes back. Note what the agent **assumed** or
   **invented**: Which charts did it pick? What file structure? Which
   library? Did it ask you anything?

Nothing is wrong with your agent — it filled every gap in your prompt with
a guess. Keep this plan (or a screenshot); you'll compare against it in
Part D.

> 💬 **Share-out**: paste the funniest or most dangerous assumption your
> agent made into the workshop chat.

## Part B — Give the agent a memory

1. Open `CLAUDE-template.md`. Most of it is written; **three spots are
   yours to complete** (marked with `✏️ TODO`).
2. Fill them in, then save the completed file as **`CLAUDE.md` in the repo
   root** (next to `pyproject.toml`).

> 🔧 Tool note: Claude Code reads `CLAUDE.md` automatically. Gemini CLI
> reads `GEMINI.md`, and several tools read `AGENTS.md` — same content,
> different filename. Save the one your tool uses (or both, they're tiny).

## Part C — Write the real brief

1. Open `requirements-card.md`. This is your project spec: the KPIs, the
   filters, the required file structure, the tech stack.
2. Write your own brief in a scratch file or directly in your agent's
   input. Build it from four ingredients:
   - **Context** — what the data is, what we're building, who it's for
   - **Requirements** — transplant the requirements card (don't retype —
     copy it)
   - **Constraints** — what the agent must not do, what to ask about
   - **Checkpoint** — require a plan first and approval before any code

The last ingredient is the one everyone forgets. Without it, the agent
starts building immediately — and you've lost your review moment.

## Part D — Review the plan, then release the agent

1. Send your brief. The agent replies with a plan (because you demanded
   one).
2. Review it against this checklist:
   - [ ] File structure matches the requirements card **exactly**
     (`app.py`, `data_loader.py`, `views/` with the four named files)
   - [ ] The 12 CSVs are loaded **once**, concatenated, and cached — not
     re-read by every view
   - [ ] All four KPIs and all three filters are accounted for
   - [ ] Environment setup (uv, dependencies) is part of the plan
   - [ ] Any assumption you disagree with? Say so **now** — this is the
     cheapest moment to change course
3. Compare it with the Part A plan. Same agent, same task, same data.
   The difference is entirely your brief.
4. Reply with your corrections, or approve: *"Plan approved — go ahead."*
5. Let the agent build. **Don't wait for it** — we continue with the next
   block while it works.

---

## ✅ Success criteria

- Your brief contains all four ingredients (context, requirements,
  constraints, checkpoint)
- Your agent proposed a plan **before** writing code
- The approved plan matches the required file structure
- `CLAUDE.md` exists in your repo root with all three TODOs completed
- Dashboard v1 is building (or built) in `dashboard/` at the repo root

## 🚀 Stretch goal

Finished early? Ask your agent: *"What information was missing from my
brief that you had to assume?"* — then patch your brief with the answer.
You just ran a retrospective on your own prompt.

## 🆘 Stuck?

A complete annotated brief and finished `CLAUDE.md` are in
[`solutions/exercise-1/`](../../solutions/exercise-1/). Copy the solution
brief, send it to your agent, and continue — falling back is allowed and
you can study the annotations later.
