"""Flight Orders 2022 — reference Streamlit dashboard.

Run from the repo root:
    uv run streamlit run dashboard/app.py
"""

import streamlit as st

from data_loader import MONTH_LABELS, load_data
from views import channels, geography, profitability, trends

st.set_page_config(
    page_title="Flight Orders 2022",
    page_icon="✈️",
    layout="wide",
)

st.title("✈️ Flight Orders 2022")
st.caption("120,396 orders · 12 monthly CSV files · full-year 2022")

df = load_data()

# ---------------------------------------------------------------- sidebar
st.sidebar.header("Filters")

month_start, month_end = st.sidebar.select_slider(
    "Sales month range",
    options=MONTH_LABELS,
    value=("Jan", "Dec"),
)
start_num = MONTH_LABELS.index(month_start) + 1
end_num = MONTH_LABELS.index(month_end) + 1

all_channels = sorted(df["Channel"].unique())
selected_channels = st.sidebar.multiselect(
    "Channel",
    options=all_channels,
    default=all_channels,
)

journey = st.sidebar.radio(
    "Journey type",
    options=["All", "One Way", "Return"],
    index=0,
)

# ------------------------------------------------------------- filtering
mask = df["Sales Month"].between(start_num, end_num)
mask &= df["Channel"].isin(selected_channels)
if journey != "All":
    mask = mask & (df["Journey Type"] == journey)

filtered = df[mask]

st.sidebar.markdown(
    f"**{len(filtered):,}** of {len(df):,} orders selected"
)

# ------------------------------------------------------------------ tabs
tab1, tab2, tab3, tab4 = st.tabs(
    ["📈 Trends", "🛒 Channels", "💰 Profitability", "🌍 Geography"]
)
with tab1:
    trends.render(filtered)
with tab2:
    channels.render(filtered)
with tab3:
    profitability.render(filtered)
with tab4:
    geography.render(filtered)
