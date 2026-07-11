# Exercise 4 — Self-Verification

⚡ **Start here:** this exercise is **demo-first** — the presenter runs it
live, and you can follow along if you set up Playwright MCP (Part A) or
just watch and reproduce it tonight from these materials. Everything
worth learning here is in the *prompts*, and those you'll write either
way.

Until now, *you* have been the one checking the dashboard — running it,
clicking filters, eyeballing charts. In this exercise the agent gets
eyes of its own: it opens your app in a real browser, verifies it,
breaks it on purpose, fixes it in a loop, and then you save the whole
routine as a one-word command.

---

## 🎯 Goal

Connect your agent to a browser via MCP, write a verification prompt
that checks the dashboard like you would, upgrade it into a
**self-correcting loop with a retry cap**, and save it as
`/check-dashboard` — yours forever.

## 🧠 Concepts you'll use

- **MCP** — the standard that gives agents access to things (here: a
  browser). Skills teach; MCP connects.
- **Agentic loops with verifiers** — produce → check → fix → re-check
- **Termination conditions** — the retry cap that keeps loops from
  running forever (this is mini **loop engineering**)
- **Custom slash commands** — the third time you type a prompt, save it

---

## Part A — Give the agent eyes (setup)

> 👀 **Watching the demo?** Skip to Part B — nothing to install. The
> setup below is for following along live (if you did it before the
> workshop) or reproducing at home.

1. Requires Node.js. Add the Playwright MCP server to Claude Code:

   ```bash
   claude mcp add playwright -- npx @playwright/mcp@latest
   ```

2. Start a new session (CLI: exit + `claude`; VS Code: **+ New chat**)
   and type `/mcp` — you should see the playwright server with its
   tools: `browser_navigate`, `browser_snapshot`,
   `browser_take_screenshot`, `browser_click`,
   `browser_console_messages`… Those names are the whole MCP idea made
   visible: a menu of capabilities a server exposes, which any
   MCP-compatible agent can call.
3. ⚠️ First use downloads a browser (~150 MB, a few minutes) — that's
   why this belongs *before* the workshop, not during it.

> 🔧 **Gemini CLI**: same server, different config — see
> `solutions/exercise-4/mcp-setup.md`. That portability is MCP's whole
> point.

## Part B — The verification prompt

1. In one terminal, start the app and leave it running:

   ```bash
   uv run streamlit run dashboard/app.py
   ```

2. Now write your verification prompt. It should tell the agent to
   check everything *you've* been checking by hand since Exercise 1 —
   as concrete pass/fail items, not vibes. Skeleton to complete:

   ```text
   The dashboard is running at http://localhost:8501. Open it in the
   browser and verify:
   1. All four tabs (Trends, Channels, Profitability, Geography) render
      a chart containing data — not empty, not an error message.
   2. [✏️ your interactivity check — pick a filter, name the change you
      expect. Example: select Journey type = "Return" and confirm the
      Trends chart changes.]
   3. [✏️ your health check — what signal says "nothing is silently
      broken"? Hint: the browser console.]
   Report a pass/fail table with one line of evidence per item, then
   close the browser.
   ```

3. Send it and watch the transcript: the agent calls the MCP tools by
   name — navigate, snapshot, click, read console — and returns your
   table. That table should look familiar: it's Exercise 3's reviewer
   discipline, pointed at a *running app* instead of source code.

## Part C — Break it, then close the loop

A verifier that only ever says PASS is unproven. Test it the way
engineers test alarms: set a small fire.

1. Sabotage (one line):

   ```text
   Introduce a small realistic bug in exactly one file under
   dashboard/views/: rename one dataframe column reference so that view
   crashes (e.g. "Margin" → "Margins"). Tell me the file and line you
   changed, and change nothing else.
   ```

   (Notice the agent *can* do this — no hook protects `dashboard/`.
   Only `data/` is armored. Guardrails have scope; you chose it in
   Exercise 2.)

2. Now the loop — your Part B prompt plus the lines that make it
   self-correcting:

   ```text
   [your Part B verification prompt]

   If any check fails: diagnose the cause, fix the code, and verify
   again from the start. Repeat until every check passes — but attempt
   at most 3 fix-and-verify rounds. If it still fails after 3, stop and
   report what you tried and what's still broken.
   ```

3. Watch the shape of what happens: verify → FAIL (your planted bug) →
   fix → verify → PASS. One iteration, caught and repaired without you.

4. The two lines you added are **loop engineering** in miniature: a
   goal with a verifier, and a **termination condition**. Ask yourself
   what happens without "at most 3 rounds" if the agent's fix is wrong
   in a new way each time — that cap is the difference between a
   self-correcting system and an expensive infinite loop.

## Part D — Save it forever

You've now typed (or refined) that verification prompt more than once.
Rule of thumb: the third time, it becomes a command.

1. Create the file `.claude/commands/check-dashboard.md` containing
   exactly your Part C loop prompt (the whole thing, verification +
   loop + cap).
2. New session, then type:

   ```text
   /check-dashboard
   ```

3. That's it. The prompt you engineered is now a one-word tool — for
   this project, forever, for anyone who clones the repo (if you commit
   the command file). After any future change to the dashboard:
   `/check-dashboard`.

> 💬 **Share-out**: paste your loop's FAIL→fix→PASS moment into the
> chat — which check caught your planted bug?

---

## ✅ Success criteria

- `/mcp` lists the playwright server and its browser tools (if you set
  up)
- Your verification prompt has ≥3 concrete pass/fail checks including
  one interaction and one console check
- The loop caught the planted bug and fixed it within the retry cap
- `.claude/commands/check-dashboard.md` exists and runs as
  `/check-dashboard`

## 🚀 Stretch goal

Make the loop's report append to a `verification-log.md` file with a
timestamp — now you have an audit trail across sessions. (And if you're
curious about parameterized commands — `/check-dashboard 8502` for a
different port — look up `$ARGUMENTS` in your tool's custom-command
docs; one placeholder is all it takes.)

## 🆘 Stuck?

The completed command file, a full working verification prompt, and
per-tool MCP setup are in
[`solutions/exercise-4/`](../../solutions/exercise-4/). Watching the
demo *is* doing this exercise — reproduce it tonight.
