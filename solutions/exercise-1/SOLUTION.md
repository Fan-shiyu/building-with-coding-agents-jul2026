# Exercise 1 — Solution: the annotated brief

Below is a complete brief that reliably produces the reference dashboard
structure. The **📝 notes explain why each part is there** — the notes are
the actual lesson; the brief is just one good way to apply them.

If you're using this as a fallback: copy the text in the box, send it to
your agent, review the plan it returns, approve, and continue with the
workshop.

---

## The brief

```text
CONTEXT
We're building a Streamlit dashboard for a travel-booking dataset:
12 monthly CSV files in data/ (sales_2022_01.csv … sales_2022_12.csv),
about 120,000 flight orders from 2022 with no missing values. The
audience is business analysts who want to explore orders, margin, and
channel performance interactively. This is a workshop project — clear,
readable code matters more than cleverness.

REQUIREMENTS
[paste the full requirements card here — KPI views, filters, file
structure, tech stack, quality baseline]

CONSTRAINTS
- The data/ folder is read-only: never modify, move, or rewrite the CSVs.
- Use only Streamlit, Plotly, and pandas. Ask before adding anything else.
- Do not read, copy from, or modify the solutions/ folder — build fresh from this brief only.
- Keep each file under ~80 lines; prefer simple, readable code.

CHECKPOINT
Before writing any code: propose your implementation plan — the files
you'll create, how you'll load and cache the 12 CSVs, and any assumptions
you're making. List any questions you have. Wait for my approval, then
set up the environment with uv and build.
```

---

## Why each part is there

**📝 CONTEXT — three sentences, three jobs.** What the data is (so the
agent doesn't have to guess or explore blindly), who it's for (business
analysts → interactive, readable, no jargon), and what kind of project
this is (workshop → simple beats clever). Without an audience, "make it
professional" is undefined; with one, the agent can make taste decisions
in the right direction.

**📝 REQUIREMENTS — transplanted, not summarized.** The requirements card
goes in verbatim. Every detail you summarize away ("four views about
sales") becomes a guess the agent makes ("I'll do revenue by weekday!").
Copy-paste is not lazy here — it's precision. The exact file names are
the load-bearing part: the later exercises point subagents, verification,
and evaluation at these files by name.

**📝 CONSTRAINTS — the "do not" list.** Notice these are all things a
well-meaning agent plausibly does: "fixing" a CSV date format, adding a
convenient library, "improving" the solutions folder. A constraint you
state costs one line; the same constraint discovered after the fact costs
a rebuild. The solutions rule says "read" and not just "modify" for a
reason: agents explore the repo before building, and if a finished
example exists they will quietly mirror it — harmless for correctness,
but then the plan you review reflects the example's choices, not your
brief. (In Exercise 2 we'll upgrade the data rule from a polite
request to a hook the agent physically cannot bypass.)

**📝 CHECKPOINT — the ingredient everyone forgets.** This one line changes
the interaction from "gamble, then react" to "review, then release." Note
it asks for three specific things: the file list (catches structure
drift), the load strategy (catches the load-12-CSVs-in-every-view
mistake), and assumptions + questions (surfaces what the agent would
otherwise silently invent). "Wait for my approval" is explicit — some
agents treat a plan request as a formality and keep going.

---

## What a good plan looks like (and what to correct)

A healthy plan for this brief mentions: the exact file structure from the
card · loading the CSVs once in data_loader.py with @st.cache_data ·
filters living in app.py and the filtered dataframe passed to views ·
environment setup as step one · usually one or two sensible questions.

Corrections we'd expect you to make if they appear:

| If the plan says… | Reply with… |
|---|---|
| "I'll create dashboard/src/…" or different file names | "Use exactly the file structure in the requirements — no src/ folder." |
| "Each view will read the CSVs it needs" | "Load once in data_loader.py, cache it, pass the dataframe down." |
| "I'll use matplotlib for the charts" | "Plotly only, as specified." |
| "I'll also clean up the data files" | "data/ is read-only — work with copies in memory." |

If the plan is good: *"Plan approved — go ahead."* Resist the urge to add
new wishes at this point; scope added during approval is how builds
drift.

---

## Completed CLAUDE.md

See [`CLAUDE-example.md`](CLAUDE-example.md) in this folder for a finished
version of the Part B template, with the three TODOs resolved and short
notes on the choices.
