# Exercise 2 — Solution: annotated

Two artifacts live in this folder alongside these notes:
[`ui-style-SKILL.md`](ui-style-SKILL.md) (a complete 8-rule skill — save
as `.claude/skills/ui-style/SKILL.md`) and
[`settings.json`](settings.json) (the finished hook config — save as
`.claude/settings.json`, with the script at
`.claude/hooks/block_data_edits.py`).

If you're using this as a fallback: copy both into place, restart your
agent session, and continue with Parts B and D of the exercise.

---

## Part A/B — Why the skill works

**📝 The description is the trigger, not decoration.** The agent reads
only descriptions at session start (progressive disclosure); the full
file loads when your request matches. That's why the description names
the *situations* ("creating, modifying, or restyling charts, layout, or
visual design") rather than summarizing the rules. A description that
just said "style rules" might not fire on "improve the visual design."

**📝 Good rules are checkable.** Look at rule 1 in the solution skill:
"titles state the insight." You can look at any chart and answer
yes/no. "Make it look professional" — the phrase from Exercise 1's bad
prompt — is not checkable, which is exactly why it produced guesses.
The craft of skill-writing is converting taste into checkable
statements. (This matters again in Exercise 5, where checkable
statements become your evaluation rubric.)

**📝 The deliberate palette gap.** The Set2 palette line lives in
CLAUDE.md, not the skill. Division of labor: one-line conventions true
for *every* session → CLAUDE.md (always loaded, so keep it lean).
Detailed how-to for *one kind of work* → skill (loaded only when doing
that work). Your two files now demonstrate the token-economics story
with your own project.

**📝 Why the fresh session in Part B.** Skills are discovered at session
start. Mid-session file creation may not register — the single most
common "my skill doesn't work" cause.

## Part C/D — How the hook mechanics flow

```
You send a request
  → agent decides to call Edit on data/sales_2022_03.csv
    → BEFORE the edit runs, Claude Code matches the tool name
      against your matcher ("Edit|Write|MultiEdit")
      → match! → runs block_data_edits.py with the call as JSON on stdin
        → script sees the path is under data/ → prints reason, exits 2
          → the edit NEVER EXECUTES; the agent receives the reason
            → agent tells you it can't modify data files
```

**📝 The two TODO answers.** Matcher: `Edit|Write|MultiEdit` — the three
tools that change file contents. Not `Read`/`Glob`/`Grep`: reading is
harmless, and hooking it would slow every exploration for zero
protection. Protected prefixes: `["data/"]` — the irreplaceable source
data. (Add `"solutions/"` if you like — the reference materials deserve
the same protection.)

**📝 Exit code 2 is the whole trick.** The script's *stderr* becomes the
agent's explanation. Write it helpfully — "this folder is read-only,
work with copies in memory" tells the agent what to do *instead*, so it
recovers gracefully rather than retrying.

**📝 What you should see in Part D.** Round 1 usually ends at the
instruction layer — many agents refuse without attempting the edit, and
strong ones first verify the claim ("I scanned the file; the dates are
already clean ISO format") before declining on principle. That refusal
IS lesson one, not a failed test. Round 2 (the tripwire) is where the
hook itself fires; expect Claude Code to report:

> PreToolUse:Write hook error: BLOCKED by hook: 'scratch/test.txt' is
> inside the protected 'scratch/' folder. This folder is read-only -
> work with copies in memory instead.

...and scratch/ is never created: the block happens before any
filesystem write.

A good stderr message still pays off here: "work with copies in memory
instead" tells the blocked agent what to do next, so it reroutes rather
than retries.

**📝 Honest limits (worth knowing, and worth one slide beat).** This
hook watches file-editing *tools*. An agent could still change a file
through the Bash tool (`sed -i ...`) — matcher-based guardrails have
scope, and defense in depth is why the soft rule stays in CLAUDE.md even
after the hook exists. Production setups add a Bash matcher with command
inspection; that's beyond today, but now you know the shape of the
problem. Also keep hook messages ASCII-only — fancy dashes and emoji can
garble in Windows consoles, and a garbled reason is a reason the agent
can't read.

**📝 Gemini CLI pointer.** Gemini CLI supports hooks with a different
config format (see its docs under hooks/custom commands). The concept —
event, matcher, command, verdict — transfers unchanged; only the JSON
shape differs.

## Troubleshooting

| Symptom | Cause → fix |
|---|---|
| Skill never triggers | Session started before the file existed → start a new session (CLI: exit + `claude`; VS Code: + New chat). Or file not at `.claude/skills/ui-style/SKILL.md` → check the path, note the leading dot. |
| Hook never fires | Same: start a new session (CLI: exit + `claude`; VS Code: + New chat). Or `settings.json` not at `.claude/settings.json`. Or matcher still says `TODO`. |
| Hook fires on everything | Matcher includes `Read` — remove it. |
| Part D edit goes through | Script path wrong in settings.json, or `PROTECTED_PREFIXES` still `["TODO/"]`. |
| Restyle changed the charts' data | Your skill has no "don't change data logic" rule — the solution's rule 8 exists for exactly this. Add it and re-run. |
