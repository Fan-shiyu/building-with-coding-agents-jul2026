# Rubric template (Part A)

Complete the six ✏️ TODO rows, then paste the whole rubric into the
Part B grading prompt. Keep every mechanical criterion **decidable**: a
stranger (or an agent) must be able to answer PASS/FAIL from evidence,
without asking you what you meant.

---

```text
RUBRIC — "a good Flight Orders dashboard"

| # | Criterion | Check method | Verdict | Evidence |
|---|-----------|--------------|---------|----------|
| 1 | The app serves at localhost:8501 and the page title is
      "Flight Orders 2022" (right app, not just *an* app) | browser | | |
| 2 | Each of the three sidebar filters (month range, channel, journey
      type) visibly changes the displayed data when used | browser | | |
| 3 | The browser console shows zero errors during a full pass through
      all four tabs | browser | | |
| 4 | ✏️ TODO — Trends view: what exactly must it show, and what must
      its title do? | browser or code | | |
| 5 | ✏️ TODO — Channels view: name the chart type and the one thing a
      reader must be able to tell from it | browser or code | | |
| 6 | ✏️ TODO — Profitability view: which two numbers must be visible
      as metrics? (You know them by heart by now.) | browser or code | | |
| 7 | ✏️ TODO — Geography view: how many countries, which order, what
      must hover show? | browser or code | | |
| 8 | ✏️ TODO — ASPIRATIONAL: something the dashboard should do but
      does NOT yet. Suggestion: "A user can download the currently
      filtered data as a CSV from the sidebar." Designed to FAIL
      today — it measures the gap, not the glory. | browser | | |
| 9 | ✏️ TODO — JUDGMENT: something real but not mechanical.
      Suggestion: "Someone seeing this dashboard cold would understand
      each chart's takeaway from its title alone." | judgment | | |
```

---

### Writing tips

- Rows 4–7: steal from your own artifacts — the requirements card
  (Exercise 1) says what each view must contain; your ui-style skill
  (Exercise 2) says what its title and hover must do. A rubric is those
  promises, made gradeable.
- Row 8: pick something you'd genuinely build next. The FAIL should
  sting a little — that's how you know it's a real criterion and not a
  softball.
- Row 9: expect the verdict to be arguable. That's the property being
  demonstrated, not a flaw in your rubric.
