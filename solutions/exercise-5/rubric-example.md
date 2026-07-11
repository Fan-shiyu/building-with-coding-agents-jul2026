# Exercise 5 — Solution: completed rubric

Paste the block below into the Part B grading prompt as-is. Your rows
4–9 will differ in wording — what matters is that each mechanical row is
decidable from evidence.

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
| 4 | The Trends view shows monthly orders AND total margin on one
      chart, and its title states an insight (e.g. names the peak),
      not an axis label | browser | | |
| 5 | The Channels view is a bar chart from which a reader can tell
      which channel contributes the most total margin | browser | | |
| 6 | The Profitability view shows the % of negative-margin orders AND
      the median margin per order as metric cards | browser | | |
| 7 | The Geography view shows exactly the top 10 destination countries
      by orders, largest on top, with total margin on hover | browser
      or code | | |
| 8 | ASPIRATIONAL: a user can download the currently filtered data as
      a CSV from the sidebar | browser | | |
| 9 | JUDGMENT: someone seeing this dashboard cold would understand
      each chart's takeaway from its title alone | judgment | | |
```

Notes on the choices: rows 4–7 restate the requirements card and the
ui-style skill's promises in gradeable form (one decidable fact per
row, no "looks good"). Row 8 is genuinely absent from the reference
build — its FAIL is correct behavior. Row 9's verdict is expected to be
arguable; that's the property on display.
