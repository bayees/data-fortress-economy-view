from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback, dash_table
from dash.dependencies import Input, Output, State

BudgetTable = html.Div(
    className="col-md-12 col-lg-12 mb-md-0 mb-12 card-chart-container",
    children=[
        html.Div(
            className="card",
            children=[
                html.Div(
                    className="card-header card-m-0 me-2 pb-3",
                    children=[
                        html.H4(
                            "Standings in WorldCups",
                            className="card-title m-0 me-2",
                            style={"font-size": "1.5vw"},
                        ),
                    ],
                ),
                html.Div(
                    className="table-responsive text-nowrap overflow-auto",
                    children=[html.Div(id="budget-table", children=[])],
                ),
            ],
        )
    ],
)


@callback(
    Output("budget-table", "children"),
    Input("year-select", "value"),
    State("budget-df", "data"),
)
def update_table(query_year, budget_df):
    df = pd.read_json(budget_df)

    df = df.loc[(df.year == int(query_year)) & (df.category_type == "Expense")]

    pivot_df = pd.pivot_table(
        df.loc[df.year == int(query_year)],
        values="amount",
        index=["category"],
        columns=["month_name_short"],
        aggfunc=sum,
    ).reset_index()

    pivot_df["Year Total"] = (
        pivot_df["Jan"]
        + pivot_df["Feb"]
        + pivot_df["Mar"]
        + pivot_df["Apr"]
        + pivot_df["May"]
        + pivot_df["Jun"]
        + pivot_df["Jul"]
        + pivot_df["Aug"]
        + pivot_df["Sep"]
        + pivot_df["Oct"]
        + pivot_df["Nov"]
        + pivot_df["Dec"]
    )

    pivot_df = pivot_df.sort_values(by=["Year Total"], ascending=True)

    pivot_df = pivot_df.fillna(0)

    pivot_df.loc[
        :,
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
            "Year Total",
        ],
    ] = pivot_df[
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
            "Year Total",
        ]
    ].applymap(
        "{:,.2f}".format
    )

    return dbc.Table.from_dataframe(
        pivot_df,
        columns=["category", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Year Total"],
        header=["Category", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Year Total"],
        class_name="no-footer",
        striped=False,
        bordered=False,
        hover=True,
        responsive=True,
    )
