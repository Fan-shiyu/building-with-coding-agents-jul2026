---
name: ui-style
description: Use this skill whenever creating, modifying, or restyling
  charts, layout, or visual design in the Streamlit dashboard. Covers
  chart composition, labeling, formatting, and layout conventions.
---

# UI & chart style conventions for this dashboard

The color palette (Plotly Set2) is set project-wide in CLAUDE.md; this
skill covers everything the palette doesn't.

## Rules

1. Chart titles state the insight, not the axis names — "Summer bookings
   peak in August", not "Orders by month".
2. Large numbers are formatted for humans: $1.2M and 12.4k — never raw
   floats like 1234567.891.
3. Every hover tooltip shows the exact value with its unit ($, orders,
   %) — hover is where precision lives, so the chart itself can stay
   clean.
4. No legend when color encodes the same thing as an axis label (a bar
   chart of channels doesn't need a channel legend).
5. Horizontal gridlines only, and subtle; vertical gridlines are off.
6. Every chart carries a one-sentence caption underneath saying what to
   look for — written for someone seeing the chart for the first time.
7. More than 10 categories in one chart → show the top 10 and say so in
   the title.
8. Restyling never changes what the data says: same aggregations, same
   filters, same numbers — if a restyle would alter a value shown,
   stop and ask first.
