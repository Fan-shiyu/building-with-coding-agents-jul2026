---
description: Verify the running dashboard in a browser and fix what fails
  (max 3 rounds)
---

The dashboard is running at http://localhost:8501. Open it in the
browser and verify:

1. All four tabs (Trends, Channels, Profitability, Geography) render a
   chart containing data — not empty, not an error message.
2. Select Journey type = "Return" in the sidebar and confirm the Trends
   chart's numbers change in response.
3. Read the browser console and confirm there are zero errors.

Report a pass/fail table with one line of evidence per item.

If any check fails: diagnose the cause, fix the code, and verify again
from the start. Repeat until every check passes — but attempt at most 3
fix-and-verify rounds. If it still fails after 3, stop and report what
you tried and what is still broken.

When everything passes (or you stop at the cap), close the browser.
