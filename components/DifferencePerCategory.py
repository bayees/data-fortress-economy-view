import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import callback
import dash_mantine_components as dmc

DifferencePerCategory = html.Div(
    className="card-chart-container col-lg-12 md-12 sm-12",
    children=[
        html.Div(
            className="card-chart",
            children=[
                html.H4(
                    "Expense per category",
                    className="card-header card-m-0 me-2 pb-3",
                    style={"font-size": "1.5vw"},
                ),
                html.Div(id="difference-per-category", children=[]),
            ],
        )
    ],
    style={"min-height": "26.25rem"},
)


@callback(
    Output("difference-per-category", "children"),
    Input("month-select", "value"),
    State("actuals-df", "data"),
    State("budget-df", "data"),
)
def update_figures(query_month, actuals_data, budget_data):
    actuals_df = pd.read_json(actuals_data)
    budget_df = pd.read_json(budget_data)

    budget_df = budget_df.loc[
        (budget_df.month == query_month) & (budget_df.category_type == "Expense")
    ]
    actuals_df = actuals_df.loc[
        (actuals_df.month == query_month) & (actuals_df.category_type == "Expense")
    ]

    df_actuals_grouped = (
        actuals_df.groupby(["month", "category"])["amount"].sum().reset_index()
    )
    df_budget_grouped = (
        budget_df.groupby(["month", "category"])["amount"].sum().reset_index()
    )

    df_details = df_actuals_grouped.merge(
        df_budget_grouped,
        how="outer",
        left_on=["month", "category"],
        right_on=["month", "category"],
        suffixes=("_actual", "_budget"),
    )
    df_details = df_details.loc[
        (df_details.amount_actual != 0) & (df_details.amount_budget != 0)
    ]

    df_details["amount_actual"] = df_details["amount_actual"].apply(lambda x: -x)
    df_details["amount_budget"] = df_details["amount_budget"].apply(lambda x: -x)

    df = (
        df_details.groupby(["category"])[["amount_actual", "amount_budget"]]
        .sum()
        .reset_index()
        .sort_values(by="amount_actual", ascending=False)
    )
    df["difference"] = df["amount_budget"] - df["amount_actual"]
    df["percentage_difference"] = df["amount_actual"] / df["amount_budget"] * 100
    df["percentage_difference_formatted"] = df["percentage_difference"].map(
        "{:.0f}%".format
    )
    df["amount_actual_formatted"] = df["amount_actual"].map("{:,.2f}".format)
    df["amount_budget_formatted"] = df["amount_budget"].map("{:,.2f}".format)
    df["difference_formatted"] = df["difference"].map("{:,.2f}".format)

    df.loc[(df["amount_budget"] > 0) & (df["difference"] < 0), "ratio_on_budget"] = (
        100 / df["percentage_difference"] * 100
    )
    df.loc[(df["amount_budget"] > 0) & (df["difference"] >= 0), "ratio_on_budget"] = df[
        "percentage_difference"
    ]
    df.loc[(df["amount_budget"] == 0) & (df["difference"] < 0), "ratio_on_budget"] = 0

    df.loc[(df["amount_budget"] > 0) & (df["difference"] < 0), "ratio_over_budget"] = (
        (df["percentage_difference"] - 100) / df["percentage_difference"] * 100
    )
    df.loc[(df["amount_budget"] > 0) & (df["difference"] >= 0), "ratio_over_budget"] = 0
    df.loc[
        (df["amount_budget"] == 0) & (df["difference"] < 0), "ratio_over_budget"
    ] = 100
    df.loc[
        (df["amount_budget"] == 0) & (df["difference"] < 0),
        "percentage_difference_formatted",
    ] = "100%"

    table_header = [
        html.Thead(
            html.Tr(
                [
                    html.Th("Category"),
                    html.Th("Amount actual", className="d-none d-sm-table-cell"),
                    html.Th("Amount budget", className="d-none d-sm-table-cell"),
                    html.Th("difference", className="d-none d-sm-table-cell"),
                    html.Th("Percentage difference"),
                ]
            )
        )
    ]

    table_rows = []
    for index, row in df.iterrows():
        table_rows.append(
            html.Tr(
                [
                    html.Td(row["category"]),
                    html.Td(
                        row["amount_actual_formatted"],
                        style={"text-align": "right"},
                        className="d-none d-sm-table-cell",
                    ),
                    html.Td(
                        row["amount_budget_formatted"],
                        style={"text-align": "right"},
                        className="d-none d-sm-table-cell",
                    ),
                    html.Td(
                        row["difference_formatted"],
                        style={"text-align": "right"},
                        className="d-none d-sm-table-cell",
                    ),
                    # html.Td(
                    #     dbc.Progress(
                    #         [
                    #             dbc.Progress(
                    #                 value=row["ratio_on_budget"],
                    #                 color="#349934",
                    #                 bar=True,
                    #                 label=row["percentage_difference_formatted"]
                    #                 if row["ratio_on_budget"]
                    #                 >= row["ratio_over_budget"]
                    #                 else None,
                    #             ),
                    #             dbc.Progress(
                    #                 value=row["ratio_over_budget"],
                    #                 color="danger",
                    #                 bar=True,
                    #                 label=row["percentage_difference_formatted"]
                    #                 if row["ratio_on_budget"] < row["ratio_over_budget"]
                    #                 else None,
                    #             ),
                    #         ],
                    #         style={"height": "20px"},
                    #     )
                    # ),
                    html.Td(
                        dmc.Progress(
                            size="xl",
                            sections=[
                                {"value": row["ratio_on_budget"], "color": "#7ac27a", "label": row["percentage_difference_formatted"] if row["ratio_on_budget"] >= row["ratio_over_budget"] else None},
                                {"value": row["ratio_over_budget"], "color": "#FF726E", "label": row["percentage_difference_formatted"] if row["ratio_on_budget"] < row["ratio_over_budget"] else None},
                            ],
                        ),
                    ),
                ]
            )
        )

    table_body = [html.Tbody(table_rows)]

    return dbc.Table(table_header + table_body, className="details-table")
