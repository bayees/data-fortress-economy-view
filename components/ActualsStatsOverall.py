from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback
from dash.dependencies import Input, Output, State
from utils.consts import actuals
import datetime

period_select_card = html.Div(
    className="col-lg-3 col-md-6 col-sm-12 card-chart-container",
    children=[
        html.Div(
            className="card",
            children=[
                html.Div(
                    className="card-body",
                    children=[
                        html.Div(
                            className="d-flex justify-content-between",
                            children=[
                                html.Div(
                                    className="card-info",
                                    children=[
                                        dbc.Select(
                                             id="month-select",
                                             value=actuals.month.max(),
                                             options=[
                                                 {"label": l, "value": l} for l in actuals.month.sort_values(ascending=False).unique()
                                             ],
                                             style={"width": "10rem"},
                                        ),
                                        html.P(
                                            className="card-text mb-1 mt-1 fs-sm",
                                            id="latest-transaction-text",
                                            children=[f"Latest transaction: "],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="card-icon d-flex align-items-center w-40 justify-content-center p-1",
                                    children=[
                                        html.Img(
                                            className="img-fluid bx-lg",
                                            id="team-flag-main",
                                            src="./assets/images/calendar.png",
                                            style={
                                                "width": "2.5em",
                                            },
                                        ),
                                    ],
                                ),
                            ],
                        )
                    ],
                )
            ],
            style={"min-height": "11rem"},
        )
    ],
)


total_budget_card = html.Div(
    html.Div(
        className="card",
        children=[
            html.Div(
                className="card-body",
                children=[
                    html.Div(
                        className="d-flex justify-content-between",
                        children=[
                            html.Div(
                                className="card-info w-100",
                                children=[
                                    html.H2(
                                        className="mb-2 mt-2 card-title mb-2",
                                        id="total-month-budget-text",
                                        style={"font-size": "2.5vw"},
                                    ),
                                    html.H6(
                                        className="card-text m-0",
                                        children=["Total budget"],
                                        style={"font-size": "1vw"},
                                    ),
                                    html.Small(
                                        className="card-text",
                                        id="winning-years-text",
                                        style={"font-size": "0.6rem"},
                                    ),
                                ],
                                style={"text-align": "center"},
                            ),
                            html.Div(
                                className="card-icon d-flex align-items-center",
                                children=[
                                    html.Img(
                                        className="img-fluid bx-lg",
                                        src="./assets/images/prince.png",
                                        style={"width": "10rem"},
                                    )
                                ],
                            ),
                        ],
                    )
                ],
            )
        ],
        style={"min-height": "11rem"},
    ),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",
)

total_expense_card = html.Div(
    html.Div(
        className="card",
        children=[
            html.Div(
                className="card-body",
                children=[
                    html.Div(
                        className="d-flex justify-content-between",
                        children=[
                            html.Div(
                                className="card-info w-100",
                                children=[
                                    html.H2(
                                        className="mb-2 mt-2 card-title mb-2",
                                        id="total-month-expense-text",
                                        style={"font-size": "2.5vw"},
                                    ),
                                    html.H6(
                                        className="card-text m-0",
                                        children=["Total expense"],
                                        style={"font-size": "1vw"},
                                    ),
                                    html.Small(
                                        className="card-text",
                                        id="winning-years-text",
                                        style={"font-size": "0.6rem"},
                                    ),
                                ],
                                style={"text-align": "center"},
                            ),
                            html.Div(
                                className="card-icon d-flex align-items-center",
                                children=[
                                    html.Img(
                                        className="img-fluid bx-lg",
                                        src="./assets/images/correct.png",
                                        style={"width": "10rem"},
                                    )
                                ],
                            ),
                        ],
                    )
                ],
            )
        ],
        style={"min-height": "11rem"},
    ),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",
)

difference_card = html.Div(
    html.Div(
        className="card",
        children=[
            html.Div(
                className="card-body",
                children=[
                    html.Div(
                        className="d-flex justify-content-between",
                        children=[
                            html.Div(
                                className="card-info w-100",
                                children=[
                                    html.H2(
                                        className="mb-2 mt-2 card-title mb-2",
                                        id="difference-month-text",
                                        style={"font-size": "2.5vw"},
                                    ),
                                    html.H6(
                                        className="card-text m-0",
                                        children=["Difference"],
                                        style={"font-size": "1vw"},
                                    ),
                                    html.Small(
                                        className="card-text",
                                        id="winning-years-text",
                                        style={"font-size": "0.6rem"},
                                    ),
                                ],
                                style={"text-align": "center"},
                            ),
                            html.Div(
                                className="card-icon d-flex align-items-center",
                                children=[
                                    html.Img(
                                        className="img-fluid bx-lg",
                                        src="./assets/images/balance.png",
                                        style={"width": "10rem"},
                                    )
                                ],
                            ),
                        ],
                    )
                ],
            )
        ],
        style={"min-height": "11rem"},
    ),
    className="col-md-6 col-lg-3 mb-md-0 mb-4 card-chart-container",
)


ActualsStatsOverall = [
        period_select_card,
        total_budget_card,
        total_expense_card,
        difference_card,
    ]

@callback(
    Output("latest-transaction-text", "children"),
    Output("total-month-budget-text", "children"),
    Output("total-month-expense-text", "children"),
    Output("difference-month-text", "children"),
    Input("month-select", "value"),
    State("budget-df", "data"),
    State("actuals-df", "data"),
)
def update_team_select(query_month, budget_data, actuals_data):
    budget_df = pd.read_json(budget_data)
    actuals_df = pd.read_json(actuals_data)

    actuals_df = actuals_df.loc[(actuals_df.month == query_month) & (actuals_df.category_type == "Expense")]
    budget_df = budget_df.loc[(budget_df.month == query_month) & (budget_df.category_type == "Expense")]

    actuals_df['date_actual'] = pd.to_datetime(actuals_df['date_actual'])
    
    latest_transaction = f"Latest transaction: : {actuals_df.date_actual.max().date()}"
    total_budget_text = f"{-budget_df.amount.sum():,.2f}"
    total_expense_text = f"{-actuals_df.amount.sum():,.2f}"
    difference_text = f"{actuals_df.amount.sum() - budget_df.amount.sum():,.2f}"

    return latest_transaction, total_budget_text, total_expense_text, difference_text
