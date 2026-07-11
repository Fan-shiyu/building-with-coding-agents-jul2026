"""KPI 2 — Margin by channel."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def make_figure(df: pd.DataFrame) -> go.Figure:
    by_channel = (
        df.groupby("Channel")
        .agg(
            Total_Margin=("Margin", "sum"),
            Orders=("Order Number", "count"),
            Avg_Margin=("Margin", "mean"),
        )
        .reset_index()
        .sort_values("Total_Margin", ascending=False)
    )
    fig = px.bar(
        by_channel,
        x="Channel",
        y="Total_Margin",
        color="Channel",
        color_discrete_sequence=px.colors.qualitative.Set2,
        hover_data={"Orders": ":,", "Avg_Margin": ":$.2f"},
        labels={"Total_Margin": "Total margin ($)"},
        title="Total margin by sales channel",
    )
    fig.update_layout(showlegend=False)
    return fig


def render(df: pd.DataFrame) -> None:
    st.subheader("Channels")
    if df.empty:
        st.info("No orders match the current filters.")
        return
    st.plotly_chart(make_figure(df), width='stretch')
    st.caption(
        "Hover a bar to see order volume and average margin per order "
        "for each channel."
    )
