# Requirements card (Part C)

This is the project spec. Copy the box below into your brief **as-is** —
these requirements are fixed so that the later exercises (subagents,
verification, evaluation) work on everyone's dashboard.

```text
PROJECT: Streamlit dashboard for the 2022 flight-order data

DATA
- 12 monthly CSV files in data/ (sales_2022_01.csv … sales_2022_12.csv)
- ~120,000 rows total, no missing values
- Columns include: Order Number, Sales Date, Departure Date, Channel,
  Journey Type, Fare Carrier, Origin/Destination Country, Base Fare,
  Tax, Margin
- The data/ folder is READ-ONLY. Never modify, move, or rewrite the CSVs.

THE FOUR KPI VIEWS (one file each, exactly these names)
1. views/trends.py        — monthly orders and total margin over the year
                            (line chart)
2. views/channels.py      — total margin by sales channel (bar chart)
3. views/profitability.py — % of orders with negative margin (metric)
                            + margin vs. ticket value (scatter)
4. views/geography.py     — top 10 destination countries by orders
                            (horizontal bar)

FILTERS (sidebar, applied once in app.py, passed to every view)
- Sales month range (select-slider, Jan–Dec)
- Channel (multiselect, default: all)
- Journey type (radio: All / One Way / Return)

FILE STRUCTURE (exactly this, at the repo root)
dashboard/
├── app.py            — page config, sidebar filters, assembles the four
│                       views as tabs
├── data_loader.py    — loads and concatenates the 12 CSVs, adds derived
│                       fields, cached with @st.cache_data
└── views/
    ├── __init__.py
    ├── trends.py
    ├── channels.py
    ├── profitability.py
    └── geography.py

TECH STACK
- Python ≥ 3.10, dependencies managed with uv (pyproject.toml at repo root)
- Streamlit for the app, Plotly for ALL charts
- The agent sets up the environment itself (uv sync / uv add) — first step
  of the build

QUALITY BASELINE
- Every chart has a title and labeled axes
- The app runs with: uv run streamlit run dashboard/app.py
```
