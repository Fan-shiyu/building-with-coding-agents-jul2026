# Exercise 3 — Delegation

⚡ **Start here:** no files to open yet — Part A is a single question you
ask your agent. This README walks you through the rest, one step at a
time.

So far one agent has done everything. In this exercise you'll delegate:
first the *work* (parallel subagents, one per view), then the *checking*
(a reviewer that can look but never touch). The rule that makes it work:
never let the maker be the checker.

---

## 🎯 Goal

Run four subagents in parallel — each improving one view file against
your ui-style skill — then create a **read-only reviewer agent** that
audits the results and reports violations it cannot fix itself.

## 🧠 Concepts you'll use

- **Subagents** — focused agents with smaller jobs, spawned by your main
  agent
- **When NOT to delegate** — parallelism only pays when tasks are
  independent
- **The reviewer pattern** — fresh eyes, constrained by architecture
  (missing tools), not politeness

## 📦 What's in this folder

| File | What it is |
|---|---|
| `README.md` | This file — your instructions |
| `reviewer-template.md` | The reviewer subagent definition with two blanks (Part C) |

---

## Part A — Ask before you delegate

Delegation is a choice, not a default. Make your agent argue it:

```text
I want to improve all four view files in dashboard/views/. Should you
do this sequentially yourself, or delegate to parallel subagents? Argue
both sides briefly, then recommend one — considering that the views are
independent files that don't import each other.
```

Read the answer. The views *are* independent (they share only the
dataframe passed in), so parallel should win here — but notice the
sequential case the agent makes: shared context, no coordination cost,
one set of eyes. That case wins more often than the hype suggests. Today
just happens to be the other kind of day.

## Part B — Delegate the work

Send this (adjust the improvement list to your taste):

```text
Delegate in parallel: spawn one subagent per view file in
dashboard/views/ (trends.py, channels.py, profitability.py,
geography.py). Each subagent works ONLY on its own file and must not
touch any other file. Each subagent's task:

1. Verify its view honors every rule in .claude/skills/ui-style/SKILL.md
   and fix anything that doesn't.
2. Add exactly ONE improvement to its view: a more helpful empty-state
   message (what should the user do when no orders match?), a smarter
   caption, or better hover formatting — its choice, but only one.

Helper files (like theme.py) may exist in dashboard/ — leave them
unchanged. When all four subagents finish, summarize per file: what was
verified, what was fixed, and the one improvement made.
```

Watch your agent's output: you should see **four Task agents launch and
run at the same time** — that's the parallelism, live. While they work
(a few minutes), continue to Part C.

> 🔧 **Other tools (Gemini CLI etc.)**: no parallel subagent feature —
> send the same prompt minus the word "parallel" and the agent will do
> the views one at a time. Same result, slower — which is itself the
> lesson: parallelism is a speed feature, not a quality feature. Watch
> the presenter's screen for the parallel version.

## Part C — Create the reviewer

Now the checking — delegated to an agent that *cannot* fix what it
finds.

1. Open `reviewer-template.md` and fill in the **two TODOs**: which
   tools a read-only reviewer gets (this is the whole trick), and what
   single document it judges against.
2. Save the completed file as **`.claude/agents/style-reviewer.md`**.
3. Start a fresh session (CLI: exit + `claude`; VS Code: **+ New
   chat**) — agent definitions load at session start — and send:

```text
Use the style-reviewer subagent to audit all four files in
dashboard/views/ against the ui-style skill. I want the full violations
table.
```

Why can't the reviewer just fix things? Because its tool list has no
Edit in it. That's the hook lesson again, applied to agents: the
constraint lives in the architecture, not in a polite instruction. A
reviewer that can fix will fix — and start judging its own work by
turn three.

## Part D — Close the loop

The reviewer found things — even though the subagents *just* polished
against the same rules. Fresh eyes on the same standard catch what the
author missed; that's the entire argument for separating maker from
checker. Now feed the findings back:

```text
Here is the reviewer's report: [paste the violations table]
Fix ONLY what the report lists — nothing else. One change per finding.
```

That restraint line matters: a report is a scope, not an inspiration.

One special case: if a finding is a letter-vs-intent collision (the
code is right, the rule's wording is wrong), the correct fix is to
amend the rule in your skill file — then re-run the reviewer and watch
the table come back clean.

> 💬 **Share-out**: paste your reviewer's most interesting finding into
> the workshop chat — especially anything the polish pass had *just*
> touched and still got flagged.

---

## ✅ Success criteria

- Part A: your agent argued both sides before recommending
- Part B: four subagents ran (in parallel on Claude Code), each view
  gained exactly one visible improvement, no file touched by two agents
- Part C: `.claude/agents/style-reviewer.md` exists; the reviewer
  produced a violations table and **edited nothing**
- Part D: fixes applied match the report line-for-line

## 🚀 Stretch goal

Run the reviewer again after Part D — does it come back clean? You've
just built a manual verify-fix cycle. (Exercise 4 automates exactly
this.) Or: define a second specialist, e.g. a `docs-reviewer` that only
checks captions and docstrings.

## 🆘 Stuck?

The completed reviewer definition, the full delegation prompt, and the
expected shape of the violations table are in
[`solutions/exercise-3/`](../../solutions/exercise-3/). Copy, run,
continue.
