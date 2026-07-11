"""KPI 4 — Top 10 destination countries."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

TOP_N = 10


def make_figure(df: pd.DataFrame) -> go.Figure:
    top = (
        df.groupby("Destination Country")
        .agg(Orders=("Order Number", "count"), Margin=("Margin", "sum"))
        .nlargest(TOP_N, "Orders")
        .reset_index()
        .sort_values("Orders")  # smallest first -> largest on top
    )
    fig = px.bar(
        top,
        x="Orders",
        y="Destination Country",
        orientation="h",
        color_discrete_sequence=px.colors.qualitative.Set2,
        hover_data={"Margin": ":$,.0f"},
        title=f"Top {TOP_N} destination countries by orders",
    )
    return fig


def render(df: pd.DataFrame) -> None:
    st.subheader("Geography")
    if df.empty:
        st.info("No orders match the current filters.")
        return
    st.plotly_chart(make_figure(df), width='stretch')
    st.caption("Hover a bar to see the total margin for that country.")
