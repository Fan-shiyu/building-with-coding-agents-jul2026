# Flight Orders 2022 — Reference Dashboard

Reference solution for the PyLadies Amsterdam workshop
**Building with Coding Agents — Ship a Python Streamlit Dashboard**.

## Expected repo layout

The data loader searches upward from `data_loader.py` for a `data/`
directory containing the CSVs, so the dashboard works from either
location below:

```
<repo-root>/
├── data/
│   ├── sales_2022_01.csv … sales_2022_12.csv   ← the 12 monthly files
├── dashboard/            ← participants' build lives here
│   ├── app.py
│   ├── data_loader.py
│   └── views/
│       ├── __init__.py
│       ├── trends.py
│       ├── channels.py
│       ├── profitability.py
│       └── geography.py
└── pyproject.toml
```

(For the reference copy in `solutions/dashboard/`, the same loader
still finds `<repo-root>/data/` automatically.)

## Run it

From the repo root, with [uv](https://docs.astral.sh/uv/):

```bash
uv sync                                   # creates .venv from pyproject.toml
uv run streamlit run dashboard/app.py     # opens http://localhost:8501
```

Without uv:

```bash
pip install streamlit plotly pandas
streamlit run dashboard/app.py
```

## What it shows

| Tab | KPI | Chart |
|---|---|---|
| 📈 Trends | Monthly orders & total margin | Dual-axis line |
| 🛒 Channels | Total margin by sales channel | Bar |
| 💰 Profitability | % negative-margin orders (51.4% overall!) + median margin | Metric cards + fare-vs-margin scatter |
| 🌍 Geography | Top 10 destination countries by orders | Horizontal bar |

Sidebar filters (applied once in `app.py`, passed to every view):
**month range** (select-slider), **channel** (multiselect),
**journey type** (radio: All / One Way / Return).

## Verification status

- ✅ Data layer: all 12 CSVs load (120,396 rows), derived fields verified
- ✅ All four figures build on full data and filtered subsets
- ✅ App executes headlessly without exceptions (Streamlit AppTest)
- ✅ All three filters re-run the app cleanly; metrics update correctly
- ✅ Empty filter selection handled gracefully (info message, no crash)
- ⬜ **Visual review in a real browser — pending** (charts render, layout,
  colors). Suggested check with Claude Code + Chrome extension:
  *"Run this dashboard, open localhost:8501, verify all four charts
  render and the three sidebar filters work, fix anything broken."*

## Known data facts (for rubric writing)

- 120,396 orders, zero missing values in source columns
- 362 orders have a $0 ticket value → their derived `Margin %` is NaN (by design)
- 51.4% of all orders have negative margin; median margin −$0.45
- Summer peak: Jul–Aug ≈ 12.6–12.9k orders/month vs. Feb 6.8k
