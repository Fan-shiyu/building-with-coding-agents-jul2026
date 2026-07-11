"""Load and prepare the 2022 flight-order data.

The loader searches upward from this file for a `data/` directory that
contains the monthly CSVs, so it works whether the dashboard lives at the
repo root (participants' build) or in `solutions/` (reference build).
"""

from pathlib import Path

import pandas as pd
import streamlit as st

MONTH_LABELS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]


def find_data_dir() -> Path:
    """Walk up from this file until a data/ folder with the CSVs is found."""
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / "data"
        if candidate.is_dir() and any(candidate.glob("sales_2022_*.csv")):
            return candidate
    raise FileNotFoundError(
        "Could not find a 'data/' directory containing sales_2022_*.csv "
        "in any parent folder. Place the 12 CSV files in <repo-root>/data/."
    )


@st.cache_data(show_spinner="Loading 12 monthly CSV files...")
def load_data() -> pd.DataFrame:
    """Load all 12 monthly CSVs into one dataframe with derived fields."""
    data_dir = find_data_dir()
    files = sorted(data_dir.glob("sales_2022_*.csv"))
    df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)

    # Parse dates
    df["Sales Date"] = pd.to_datetime(df["Sales Date"])
    df["Departure Date"] = pd.to_datetime(df["Departure Date"])

    # Derived fields
    df["Sales Month"] = df["Sales Date"].dt.month  # 1..12
    df["Month Label"] = df["Sales Month"].map(
        lambda m: MONTH_LABELS[m - 1]
    )
    df["Total Ticket"] = df["Base Fare"] + df["Tax"]
    df["Lead Time (days)"] = (
        df["Departure Date"] - df["Sales Date"]
    ).dt.days
    df["Margin %"] = df["Margin"] / df["Total Ticket"].where(
        df["Total Ticket"] != 0
    )
    df["Route"] = (
        df["Origin Airport Code"] + " → " + df["Destination Airport Code"]
    )
    df["Domestic"] = df["Origin Country"] == df["Destination Country"]

    return df
