# Exercise 3 — Solution: annotated

The completed reviewer definition is in
[`style-reviewer.md`](style-reviewer.md) — save it as
`.claude/agents/style-reviewer.md` and start a fresh session. The
delegation prompt is in the exercise README's Part B and needs no
changes to work.

If you're using this as a fallback: copy the reviewer file into place,
run the Part B prompt as-is, then the Part C audit prompt, and continue.

---

## Part A — What a good both-sides answer contains

**For sequential**: one agent keeps full context (it just restyled these
files in Exercise 2 and remembers why choices were made); no
coordination overhead; no risk of two agents making inconsistent
choices; for four small files, the total time difference is minutes.

**For parallel**: the views are genuinely independent — separate files,
no imports between them, all consuming the same dataframe interface;
each subagent gets a small, focused context (the file + the skill)
instead of everything; wall-clock time divides by ~4.

**The tiebreaker the agent should land on**: independence. Parallel
delegation is safe *because* no two subagents can touch the same file —
the structure you locked in Exercise 1's requirements card is what makes
today's parallelism collision-free. (Sequential would not be *wrong*;
it would be slower and equally correct. Delegation is a speed feature.)

Two subtleties a sharp agent may surface: first, the sequential case's
real strength is *accumulated judgment* (having just written three
sibling files), not mere access to the rules — handing each subagent
the skill file replicates the rules, not the judgment. Second, the
honest reason parallel still wins: the reviewer in Part C is what
backstops the consistency risk. We can afford four divergent
interpretations because one standard-bearer checks them all afterward.

## Part B — Why the delegation prompt is shaped that way

**📝 "ONLY on its own file and must not touch any other file"** — the
collision rule. Parallel agents editing the same file is the classic
multi-agent failure; the prompt makes the file boundary explicit rather
than hoping the agents infer it.

**📝 "exactly ONE improvement ... its choice, but only one"** — bounded
creativity. Unbounded ("improve the view") invites scope creep times
four; zero additions would make the run invisible. One visible change
per file guarantees you can *see* that four agents did four things.

**📝 "Helper files (like theme.py) may exist — leave them unchanged"** —
your Exercise 2 restyle likely created shared helpers. Four parallel
agents all "improving" a shared helper is the collision rule's sneakiest
violation, so it's named explicitly.

**📝 The closing summary demand** — subagent results come back to the
main agent, which can silently absorb them. Requiring a per-file summary
makes the fan-out/fan-in visible to *you*.

## Part C — Why the two TODOs are the lesson

**TODO 1 answer: `tools: Read, Grep, Glob`** — the three tools that can
look; none that can change. Edit and Write are the obvious exclusions;
**Bash is the subtle one** — a "read-only" reviewer with Bash can `sed
-i` its way around the whole constraint (the same loophole Exercise 2's
hook has, now on the agent side). If you included Bash, you've built a
reviewer that can quietly become an editor.

**📝 Why architecture beats instruction here** — you could write "please
don't edit" in the body (we do, as belt-and-braces), but an agent under
pressure ("just fix that one comma while you're there") will rationalize
a quick edit. An agent *without Edit in its tool list* cannot. This is
the hook lesson transposed: constraint by configuration survives
persuasion; constraint by politeness doesn't. It also keeps the review
honest over time — a reviewer that fixes things starts reviewing its own
work, and fresh eyes stop being fresh.

**TODO 2 answer: `.claude/skills/ui-style/SKILL.md`** — the single
standard. Not CLAUDE.md (project facts, not design rules), and
explicitly not the reviewer's own taste. A reviewer with a defined
standard produces *actionable* findings ("violates rule 6"); a reviewer
judging by taste produces opinions you can't close the loop on.

**📝 The rigid output table** — file / rule # / quoted evidence /
verdict. Structured findings become Part D's work order; prose findings
become a discussion. (This table is also your first taste of Exercise
5's rubric thinking: checkable statements, evidence, verdicts.)

## Part D — What to expect

How many findings to expect depends on how thorough Exercise 2 was:
after a strong restyle, 0–3 is normal, and a clean table is a valid
result. The likeliest catch is the most interesting kind: a
letter-vs-intent collision — e.g. a maker deliberately kept value-axis
gridlines on a horizontal bar chart, judging the rule's intent over its
wording, and the reviewer (which judges by the letter, with no memory
of that reasoning) flags the same line. Neither agent is wrong: the
rule is. Amending the skill — with a horizontal-bar exception, say — is
a fully legitimate Part D fix; findings can audit the rulebook, not
just the code.

**📝 "Fix ONLY what the report lists"** — the report is a scope, not an
inspiration. Without that line, the fixing agent treats findings as a
theme ("while I'm at it...") and you lose the tight
find→fix→verify correspondence that makes the loop auditable.

## Troubleshooting

| Symptom | Cause → fix |
|---|---|
| No parallel Tasks visible in Part B | Tool doesn't support subagents (Gemini CLI → sequential is expected), or the prompt lost the word "parallel". |
| Two agents edited the same file | The "ONLY its own file" line was dropped, or a shared helper got "improved" — restore from git and re-run with the prompt as written. |
| `style-reviewer` not found in Part C | Session started before the file existed → new session (CLI: exit + `claude`; VS Code: + New chat). Or wrong path — must be `.claude/agents/style-reviewer.md`. |
| Reviewer edited a file anyway | Its `tools:` line includes Edit, Write, or Bash — remove them. The instruction alone is not the constraint; the tool list is. |
| Reviewer reports taste, not rules | TODO 2 not filled, or filled with CLAUDE.md — point it at the skill file. |
| Empty violations table | Legitimate if your skill is loose or the polish was thorough — a clean report is a valid report. Tighten one rule and re-run if you want to see it fire. |
