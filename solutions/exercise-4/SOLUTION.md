# Exercise 4 — Solution: annotated

Two artifacts live alongside these notes:
[`check-dashboard.md`](check-dashboard.md) — the completed slash command
(save as `.claude/commands/check-dashboard.md`) — and
[`mcp-setup.md`](mcp-setup.md) — Playwright MCP setup per tool.

If you're using this as a fallback or reproducing at home: do the setup,
start the app, save the command file, new session, type
`/check-dashboard`.

---

## Part A — Why the `/mcp` moment matters

**📝 The tool list IS the lesson.** When `/mcp` shows
`browser_navigate`, `browser_click`, `browser_console_messages`, you're
looking at the Model Context Protocol doing its one job: a server
exposing a menu of capabilities in a standard shape any agent can call.
The same server config works in Claude Code, Gemini CLI, Cursor —
that's the "USB-C for agents" pitch, verified on your own machine.
Contrast with Exercise 2: **skills teach the agent how; MCP gives it
hands (and here, eyes).**

**📝 Why the browser download belongs before the workshop** — 150 MB ×
30 participants × one venue's WiFi is how live demos die. Setup friction
is real; schedule it where it can't hurt.

## Part B — Why the checks are shaped that way

**📝 Concrete pass/fail, one interaction, one health signal.** "Verify
the dashboard works" invites the agent to look at the homepage and say
"seems fine." The three-check shape forces evidence: rendering (charts
contain data), behavior (a named filter produces a named change), and
silence (zero console errors — the check that catches what looks fine
but is quietly broken). Skeleton answers: check 2 — *select Journey
type = "Return" and confirm the Trends chart's numbers change*; check 3
— *read the browser console and confirm zero errors or warnings*.

**📝 "Close the browser"** — small hygiene line; without it the browser
session lingers and the next run sometimes trips over it.

**📝 The reviewer's ghost.** The pass/fail-with-evidence table is
Exercise 3's reviewer discipline transplanted from source code to a
running app. Same epistemics: defined standard, quoted evidence,
verdict. (In Exercise 5 this becomes a rubric and the standard becomes
yours.)

## Part C — The loop, annotated

**📝 Why sabotage is legitimate engineering.** A verifier that has only
ever said PASS is untested — you don't know if it *can* fail. Planting
one known bug and watching FAIL → fix → PASS is how alarm systems, unit
tests, and backup restores are validated. The rename-a-column bug is
chosen because it's realistic (the most common real breakage), visibly
crashes exactly one view, and has an unambiguous fix.

**📝 The guardrail scope beat.** The agent will happily sabotage
`dashboard/` — and would be blocked sabotaging `data/`. If a
participant asks "wait, why did it agree to break the code?", that's
the Exercise 2 lesson resurfacing: protection is where you installed
it, nowhere else.

**📝 The termination condition is the entire second lesson.** The loop
lines add exactly two things: a repeat-until-pass rule and a cap.
Without the cap: an agent whose fix is wrong in a new way each round
loops until you notice the token bill. With it: bounded cost, and a
*structured surrender* ("what I tried, what's still broken") that hands
the problem back to the human with context instead of failing silently.
That pattern — goal, verifier, repair, cap, report — is loop
engineering in one paragraph. Real-world versions add budgets and
checkpointing; the anatomy is identical.

**📝 Expected live behavior**: one iteration. Verify catches the planted
crash in the sabotaged view (checks 1 and 3 both fire — the tab shows
an exception and the console logs it), the agent reads the traceback,
restores the column name, re-verifies, all green. If the agent fixes it
*differently* than the sabotage (e.g. renames the dataframe column at
load), that still passes the loop — worth noticing that verifiers
accept any fix that satisfies the checks, which is both their power and
their blind spot.

**📝 The verification trap our own dry run hit — check identity, not
just liveness.** Two real failures, both silent: (1) a stale Streamlit
server from days earlier still held port 8501, so the browser verified
a different app than the one being edited — the health check asked 'is
something responding?' and blessed the wrong something; (2) Streamlit
does not hot-reload changed submodules, so a long-running server
rendered pre-edit code and the loop passed while the bug sat on disk.
The fixes: launch with --server.runOnSave true, kill stale servers
before verifying, and when a pass surprises you, verify *identity* —
confirm which app.py the listener actually serves, or add an identity
check (a page title or version string) to your verification prompt.
Production loop engineering treats 'am I verifying the right thing?' as
check zero.

## Part D — Why a file, why fixed

**📝 The command is captured expertise**, same species as Exercise 2's
skill — but *you* pull this trigger; the skill fires itself. (Skill =
knowledge the agent applies when relevant; command = a button you
press.) Committing `.claude/commands/` shares the button with everyone
who clones the repo.

**📝 Why no parameters**: the exercise's point is capturing a refined
prompt, not building tooling. One `$ARGUMENTS` placeholder adds ports
or URLs later — one sentence in the docs, when you need it.

## The Chrome-extension alternative (one honest paragraph)

Claude Code also integrates with the **Claude in Chrome extension**
(`claude --chrome`): same verify-fix loop, driven from the same CLI,
but steering *your real Chrome* — visible clicking, near-zero setup, no
Node or download. It's the convenience option once you understand the
machinery; we teach Playwright MCP because the machinery is the
curriculum (visible MCP tools, works in any MCP-capable agent, headless
when you want it). If you're Claude-only and paid-plan: try both, keep
whichever you reach for.

## Troubleshooting

| Symptom | Cause → fix |
|---|---|
| `/mcp` shows nothing | Server added but session predates it → new session (CLI: exit + `claude`; VS Code: + New chat). |
| First run hangs | The one-time browser download — let it finish; that's the 150 MB. |
| Agent says it can't reach the app | Streamlit not running, or a different port — check the terminal, pass the right URL. |
| Verify passes but the app looks broken to you | Your checks don't cover what you're seeing — add a check. The agent rises exactly to the standard of your verifier, never above it. |
| Loop hits the 3-round cap | Working as designed: read the surrender report, fix by hand or raise the cap once. Never remove the cap. |
| `/check-dashboard` not found | File not at `.claude/commands/check-dashboard.md`, or session predates it → new session. |
| Verifier reports on the wrong app | A stale server holds the port from an earlier session — kill all Streamlit processes, restart, and confirm the listener's command line serves dashboard/app.py, not another copy. |
| All-green immediately after sabotage | Server serving pre-edit code from memory (no submodule hot-reload) — restart it or launch with --server.runOnSave true, then re-run. |
| Orphaned servers accumulate | Every "start the app" that loses the port race leaves an idle process — periodically kill all Streamlit processes; before a live demo, always. |
