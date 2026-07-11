"""KPI 3 — Profitability: share of negative-margin orders."""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

SCATTER_SAMPLE = 5_000  # keep the scatter responsive


def make_figure(df: pd.DataFrame) -> go.Figure:
    plot_df = df[["Total Ticket", "Margin"]].copy()
    plot_df["Result"] = (plot_df["Margin"] >= 0).map(
        {True: "Profit", False: "Loss"}
    )
    if len(plot_df) > SCATTER_SAMPLE:
        plot_df = plot_df.sample(SCATTER_SAMPLE, random_state=42)

    fig = px.scatter(
        plot_df,
        x="Total Ticket",
        y="Margin",
        color="Result",
        color_discrete_map={"Profit": "#66C2A5", "Loss": "#FC8D62"},
        opacity=0.45,
        labels={"Total Ticket": "Total ticket value ($)"},
        title=(
            "Margin vs. ticket value "
            f"(random sample of {SCATTER_SAMPLE:,} orders)"
        ),
    )
    fig.add_hline(y=0, line_dash="dash", line_color="grey")
    return fig


def render(df: pd.DataFrame) -> None:
    st.subheader("Profitability")
    if df.empty:
        st.info("No orders match the current filters.")
        return

    negative_share = (df["Margin"] < 0).mean()
    median_margin = df["Margin"].median()

    col1, col2 = st.columns(2)
    col1.metric(
        "Orders with negative margin",
        f"{negative_share:.1%}",
        help="Share of filtered orders where margin is below zero.",
    )
    col2.metric(
        "Median margin per order",
        f"${median_margin:,.2f}",
    )

    st.plotly_chart(make_figure(df), width='stretch')
    st.caption(
        "Every point below the dashed line is an order sold at a loss."
    )
