# SKILL template (Part A)

Complete this file, then save it as `.claude/skills/ui-style/SKILL.md`
(delete this header block when you save).

How it works: the agent reads only the `description` at session start.
When your request matches it, the whole file gets loaded. That's why the
description matters — it's the trigger. And that's why detailed style
rules live *here* instead of CLAUDE.md: CLAUDE.md is loaded every
session no matter what (the always-paid tax); this file costs tokens
only when you're actually doing design work.

One deliberate gap: the color palette (Plotly Set2) is already in your
CLAUDE.md — a one-line convention that applies to everything. This skill
covers what a palette can't: the craft.

---

```markdown
---
name: ui-style
description: Use this skill whenever creating, modifying, or restyling
  charts, layout, or visual design in the Streamlit dashboard. Covers
  chart composition, labeling, formatting, and layout conventions.
---

# UI & chart style conventions for this dashboard

## Rules

1. Chart titles state the insight, not the axis names — "Summer bookings
   peak in August", not "Orders by month".
2. Large numbers are formatted for humans: $1.2M and 12.4k — never raw
   floats like 1234567.891.

✏️ TODO — add 4–6 rules of your own. Ideas to react to (write your
version, don't copy): what must every hover tooltip show? How much
whitespace between elements? Are gridlines in or out? Legends — when are
they allowed? What happens to a chart with more than N categories? Is
there a caption under every chart, and what does it say?

3.
4.
5.
6.
```
