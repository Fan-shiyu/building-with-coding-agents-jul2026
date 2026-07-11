# Exercise 5 — Evaluation

⚡ **Start here:** open `rubric-template.md` first — this README walks
you through the rest.

All week you've been improving your agent setup — a brief, a CLAUDE.md,
a skill, a hook, a reviewer, a verification loop. One question remains:
**is any of it actually good?** Feelings don't answer that. A rubric
does. In this final exercise you define what "a good dashboard" means,
in writing — and then a fresh agent grades your build against it, with
evidence. Everyone leaves with a scorecard.

---

## 🎯 Goal

Write an 8–9 criterion rubric for your dashboard, have a **fresh agent
instance** grade it pass/fail with evidence, and read your scorecard —
including at least one honest FAIL you planted on purpose.

## 🧠 Concepts you'll use

- **Evaluation** — a verifier judges the work; an eval judges the
  worker (your whole setup)
- **Checkable criteria** — the skill you've practiced since Exercise 2's
  rules
- **Code-check vs. LLM-as-judge** — mechanical verdicts vs. judgment
  verdicts, and why the difference matters
- **Fresh eyes** — the grader must not be the session that built it
  (Exercise 3's lesson, one last time)

## 📦 What's in this folder

| File | What it is |
|---|---|
| `README.md` | This file — your instructions |
| `rubric-template.md` | The rubric: 3 criteria given, 6 for you to write (Part A) |

---

## Part A — Write the rubric

1. Open `rubric-template.md`. Three criteria are given — you'll
   recognize them: they're your `/check-dashboard` checks, formalized.
   That's no accident. A verifier check and an eval criterion are the
   same species: a **checkable statement with a defined way to decide
   it**.
2. Write criteria 4–7: **one per KPI view**, each naming something
   specific and decidable. Compare:
   - ❌ "The trends view is good"
   - ✅ "The Trends view shows monthly orders AND total margin on one
     chart, and its title states an insight, not an axis name"
3. Write criterion 8 — **the aspirational one**. Something the
   dashboard should arguably do but *does not yet* (the template
   suggests one). This row is *designed to FAIL*. Why on earth? Because
   a rubric that only measures what you already built is a mirror, not
   an instrument. The FAIL row is the difference between "look how good
   I am" and "here's the gap, measured." Real eval suites are full of
   deliberately-not-yet-passing criteria — that's the roadmap part.
4. Write criterion 9 — **the judgment one**. Something real but not
   mechanically checkable (the template suggests one). Mark its check
   method as "judgment". This row exists so you can watch the
   difference: rows 1–8 get verdicts, row 9 gets an *opinion with
   reasoning* — useful, but noisier. That's the code-check vs.
   LLM-as-judge trade in one table.

## Part B — The grading run

1. Make sure the app is running:

   ```bash
   uv run streamlit run dashboard/app.py --server.runOnSave true
   ```

2. Start a **fresh session** (CLI: exit + `claude`; VS Code: **+ New
   chat**). Fresh matters: the session that built the dashboard grades
   it the way authors proofread their own writing — with the intent, not
   the evidence. (Exercise 3, one last time.)
3. Send this, pasting your completed rubric where marked:

   ```text
   You are grading a Streamlit dashboard against a fixed rubric. The
   app runs at http://localhost:8501. Rules:

   - Grade ONLY against the rubric below. No criteria of your own.
   - For each criterion: verdict PASS or FAIL, plus ONE line of
     evidence (a number, a quote, a screenshot observation). For the
     row marked "judgment": verdict plus two sentences of reasoning,
     and label it JUDGMENT so it's visibly different in kind.
   - Use the browser to check what needs the browser; read source code
     where that's more direct. Say which you used per row.
   - You fix NOTHING. You only grade. A FAIL is a finding, not a task.
   - Output: the rubric as a table with Verdict and Evidence columns
     filled, then a one-line overall score (n/8 mechanical rows passed — row 9 is judgment, not mechanical).

   RUBRIC:
   [paste your completed rubric here]
   ```

4. Read your scorecard. Expected shape: 8 passes and **one honest FAIL**
   (your aspirational row) — plus a judgment row you can agree or argue
   with.

> 🔧 **No browser MCP set up?** The grader can still decide most rows by
> reading source and running the app headlessly — tell it to mark
> browser-only rows SKIPPED and grade the rest. Partial evals are
> normal; note what your instrument can't see.

## Part C — Read it, share it, act on it once

1. Check the evidence lines, not just the verdicts — an eval you don't
   read is a ritual.
2. If anything failed that *shouldn't* have: that's a real finding —
   fix it (you have `/check-dashboard` for exactly this) and re-grade.
3. Your aspirational FAIL stays failed today — it's tomorrow's task,
   measured. That's the point.

> 💬 **Share-out**: paste your score line and your favorite evidence
> line into the workshop chat. Bonus: paste your aspirational
> criterion — what did you decide your dashboard should do next?

---

## ✅ Success criteria

- Your rubric has 9 rows: 3 given, 4 view-specific, 1 aspirational,
  1 judgment — every mechanical row decidable from evidence
- The grading ran in a **fresh session** and fixed nothing
- Your scorecard has evidence per row and exactly the FAILs you can
  explain
- You can say out loud what your aspirational criterion measures and
  why it's next

## 🚀 Stretch goal

Save your rubric as `.claude/commands/grade-dashboard.md` (you know
how). Now your project has TWO one-word instruments: `/check-dashboard`
asks "does it still work?"; `/grade-dashboard` asks "how good is it?"
Run the second after any big change and watch your score move over time
— that's an eval doing its real job.

## 🆘 Stuck?

A completed 9-row rubric and notes on writing checkable criteria are in
[`solutions/exercise-5/`](../../solutions/exercise-5/). Copy, grade,
continue.
