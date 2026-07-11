# Exercise 2 — Standards & Limits

⚡ **Start here:** open `SKILL-template.md` first — this README walks you
through the rest, one file per step.

In Exercise 1 you wrote a brief and the agent built your dashboard. Now
you'll upgrade how you work with it in two ways: teach it your **taste**
(a skill it applies automatically), then give it a **rule it cannot
break** (a hook that protects your data). Soft standards, hard limits.

---

## 🎯 Goal

Create a `ui-style` skill that restyles your dashboard to *your* design
rules from one vague prompt — then install a hook that makes the `data/`
folder physically untouchable, and watch it bounce a very
reasonable-sounding request.

## 🧠 Concepts you'll use

- **Skills** — expertise written down once, loaded only when relevant
- **Hooks** — guardrails enforced by the system, not by the agent's
  goodwill
- **Context economics** — CLAUDE.md is the always-paid tax; skills are
  pay-per-use

## 📦 What's in this folder

| File | What it is |
|---|---|
| `README.md` | This file — your instructions |
| `SKILL-template.md` | The skill file with room for your design rules (Part A) |
| `hook-template/settings.json` | Hook config with two blanks (Part C) |
| `hook-template/block_data_edits.py` | The checker script the hook runs — complete, read it |

---

## Part A — Write your design rules

1. Open `SKILL-template.md`. The frontmatter and two example rules are
   done; **write 4–6 rules of your own** where marked.
2. Good rules are specific and checkable. Compare:
   - ❌ "Make charts look clean"
   - ✅ "Chart titles state the insight, not the axis names —
     'Summer bookings peak in August', not 'Orders by month'"
   Think: number formatting, hover tooltips, spacing, what every chart
   must/must never have.
3. Save the completed file as **`.claude/skills/ui-style/SKILL.md`**
   (create the folders; note the leading dot).

> 🔧 **Gemini CLI**: no native skills feature — save the file anywhere
> (e.g. `skills/ui-style.md`) and in Part B add one line to the prompt:
> *"First read skills/ui-style.md and follow it."* Same concept, manual
> trigger.

## Part B — One vague prompt

1. Start a **fresh agent session** (so the skill gets discovered), then
   send exactly this — nothing more:

   ```text
   Improve the visual design of the dashboard.
   ```

2. That vagueness is the point: in Exercise 1, vague prompts produced
   guesses. Now the skill fills the gap — the agent should announce it's
   using `ui-style` and restyle to *your* rules.
3. While it works (it takes a few minutes — don't wait, continue to
   Part C), think about what would have happened without the skill.
4. When it's done: `uv run streamlit run dashboard/app.py` — compare
   against your Exercise 1 screenshots.

> 💬 **Share-out**: paste your favorite rule and what the agent did with
> it into the workshop chat. Every dashboard in this workshop now looks
> different — that's the skill difference, not the agent difference.

## Part C — Install the hard limit

1. Your brief and CLAUDE.md already *ask* the agent to leave `data/`
   alone. Asking works — until context fills up, or a request sounds
   reasonable enough. Now we make it a rule the agent can't break.
2. Read `hook-template/block_data_edits.py` — it's complete. It receives
   every file-editing tool call, checks the target path, and exits with
   code 2 (= block) if the path is protected.
3. Open `hook-template/settings.json` and fill in the **two TODOs**:
   which tools count as file edits (the matcher), and — in the script —
   which paths are protected.
4. Copy your completed files into place:
   - `settings.json` → `.claude/settings.json`
   - `block_data_edits.py` → `.claude/hooks/block_data_edits.py`
5. Restart your agent session (hooks load at session start).

> 🔧 **Gemini CLI**: hooks exist but use a different config format — see
> the pointer in the solution. The universal fallback: keep the rule in
> your context file and verify manually. (The concept is what transfers.)

## Part D — Try to break it

1. Send this perfectly reasonable-sounding request:

   ```text
   The dates in data/sales_2022_03.csv look wrong — please fix the
   format directly in the file.
   ```

2. Watch what happens: the edit is **blocked before it executes**, and
   the agent reports it isn't allowed to modify data files. It didn't
   *choose* to refuse — it *couldn't* comply.
3. That's the difference between Exercise 1's constraint (a request the
   agent reads) and a hook (a door that won't open).

> 💬 **Share-out**: paste the agent's refusal message into the chat.

---

## ✅ Success criteria

- `.claude/skills/ui-style/SKILL.md` exists with 6–8 total rules
- The vague prompt triggered the skill and the dashboard visibly changed
- The hook blocks edits to `data/` — you saw the refusal with your own
  eyes
- Your dashboard still runs

## 🚀 Stretch goal

Add one more rule to the skill and re-run the vague prompt — one-line
change, visible effect. Or theme the app shell: ask the agent to create a
`.streamlit/config.toml` with a custom `[theme]` — the parts of the look
Plotly doesn't control.

## 🆘 Stuck?

A complete 8-rule skill, the finished hook config, and the expected
refusal transcript are in
[`solutions/exercise-2/`](../../solutions/exercise-2/). Copy, install,
continue — study the annotations later.
