"""KPI 1 — Monthly orders & margin trend."""

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from data_loader import MONTH_LABELS


def make_figure(df: pd.DataFrame) -> go.Figure:
    monthly = (
        df.groupby("Sales Month")
        .agg(Orders=("Order Number", "count"), Margin=("Margin", "sum"))
        .reindex(range(1, 13))
        .reset_index()
    )
    monthly["Month"] = monthly["Sales Month"].map(
        lambda m: MONTH_LABELS[m - 1]
    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(
            x=monthly["Month"], y=monthly["Orders"],
            name="Orders", mode="lines+markers",
            line=dict(color="#66C2A5", width=3),
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=monthly["Month"], y=monthly["Margin"],
            name="Total margin ($)", mode="lines+markers",
            line=dict(color="#FC8D62", width=3, dash="dot"),
        ),
        secondary_y=True,
    )
    fig.update_layout(
        title="Monthly orders and total margin",
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
        hovermode="x unified",
    )
    fig.update_yaxes(title_text="Orders", secondary_y=False)
    fig.update_yaxes(title_text="Total margin ($)", secondary_y=True)
    fig.update_xaxes(title_text="Sales month (2022)")
    return fig


def render(df: pd.DataFrame) -> None:
    st.subheader("Trends")
    if df.empty:
        st.info("No orders match the current filters.")
        return
    st.plotly_chart(make_figure(df), width='stretch')
    st.caption(
        "Orders and margin move together through the year; "
        "note the summer peak in July–August."
    )
