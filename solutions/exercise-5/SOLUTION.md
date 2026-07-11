# Exercise 5 — Solution: annotated

The completed rubric is in [`rubric-example.md`](rubric-example.md) —
paste it into the Part B grading prompt as-is if you're using this as a
fallback.

---

## Why the rubric is shaped that way

**📝 Rows 1–3 are your `/check-dashboard` checks, formalized — on
purpose.** The reveal of this exercise is that you've been doing
evaluation all week without the name: a verifier check and an eval
criterion are the same species (checkable statement + defined decision
method). The difference is scope and tense: the verifier gates *this
change, now*; the eval measures *the whole build, over time*. Same
rows, two instruments.

**📝 Row 1 checks identity, not liveness.** "The page title is 'Flight
Orders 2022'" exists because our own dry runs got burned twice by
verifying the wrong thing (a stale server on the port; stale code in
memory). Check zero of any eval: am I measuring the thing I think I'm
measuring?

**📝 Rows 4–7 are the requirements card, made gradeable.** Notice the
circle closing: Exercise 1's brief promised these views; Exercise 5
measures the promises. A rubric is a brief's afterlife. This is also
why fixed KPIs made the workshop composable — everyone's rubric can
name the same charts.

**📝 Row 8, the designed FAIL, is the intellectually honest row.** A
rubric built only from what already passes is a mirror — it can't
detect regress (nothing distinguishes "still good" from "the eval is
too easy") and it can't guide progress. The deliberate gap turns the
scorecard from a trophy into a roadmap. In real eval suites this is
standard: aspirational criteria sit at FAIL until the work catches up,
and the day one flips to PASS *is the progress signal*. If your row 8
passed on the first grading, it wasn't aspirational — write a harder
one.

**📝 Row 9 exists to make a limitation visible, not to be reliable.**
Mechanical rows produce verdicts; the judgment row produces an opinion
with reasoning — plausibly correct, visibly arguable, and it can differ
between runs. That's LLM-as-judge in one row: use it for what code
can't check (clarity, tone, would-a-stranger-get-it), never for what
code can, and never alone for anything that matters. If you re-run the
grading and row 9 flips while rows 1–8 hold, you've just seen judge
noise with your own eyes — worth one share-out.

## Why the grading prompt is shaped that way

**📝 "Grade ONLY against the rubric — no criteria of your own"** — the
Exercise 3 reviewer discipline, inherited. An eval's authority comes
from its fixedness; a grader that improvises criteria is a critic, and
critics can't be compared across runs.

**📝 "You fix NOTHING"** — same separation as the read-only reviewer,
for the same reason: a grader that fixes starts grading its own
work, and your scorecard stops meaning anything. (Here it's held by
instruction rather than tool restriction — if you want it
architectural, define a grader agent with `tools: Read, Grep, Glob` +
the browser tools. Stretch of the stretch.)

**📝 "Say which method you used per row"** — makes the evidence
auditable and teaches the two-instrument habit: browser for behavior,
source for structure. Either alone can be fooled (this week proved it).

**📝 Why a fresh session, one last time** — the building session grades
with its intent ("I meant the title to be insightful") instead of the
evidence ("the title says…"). Fresh eyes read only what's on the page.
You've now used this principle three ways: reviewer (Ex 3), verifier
(Ex 4), grader (Ex 5). It's the same principle.

## What to expect from the grading run

On a build that went through Exercises 1–4: rows 1–7 PASS with crisp
evidence, row 8 FAIL (by design — evidence: "no download control exists
in the sidebar"), row 9 usually PASS with reasoning that quotes your
insight-titles. Score line: 8/9 mechanical — wait, 7/8 mechanical rows
plus one designed FAIL: read it as **"everything promised: delivered;
next milestone: named."** That's the emotional note the workshop ends
on — not a perfect score, a *measured* one.

## Troubleshooting

| Symptom | Cause → fix |
|---|---|
| Grader invents extra criteria | The "ONLY against the rubric" line was dropped — restore it and re-run. |
| Grader fixes a failure | Same — the "You fix NOTHING" line is load-bearing. Re-run; for architecture-level enforcement, use a restricted grader agent. |
| Row 8 passed | Your aspirational criterion already exists in the build — write a genuinely absent one. |
| Row 9 verdict feels wrong | Working as intended — argue with the reasoning, not the verdict. If it flips across runs, that's judge noise on display. |
| Grader can't use the browser | No Playwright MCP in this environment — have it mark browser-only rows SKIPPED and grade the rest from source + headless run. Partial evals are normal. |
| All-green suspiciously fast | The week's lesson: verify identity (row 1 exists for this) and make sure the server serves current code (--server.runOnSave true). |
