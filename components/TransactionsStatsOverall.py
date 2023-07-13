from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback
from dash.dependencies import Input, Output, State
from utils.data import get_actuals

actuals_df = get_actuals()

month_selector_card = html.Div(
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
                                            id="transactions-month-select",
                                            value=actuals_df["month"].max(),
                                            options=[
                                                {"label": l, "value": l}
                                                for l in actuals_df["month"].unique()
                                            ],
                                            style={"width": "10rem"},
                                        ),
                                        html.P(
                                            className="card-text mb-1 mt-1 fs-sm",
                                            id="team-code-text",
                                            children=[f"Team Code: "],
                                        ),
                                        html.P(
                                            className="card-text mb-1 fs-sm",
                                            id="team-region-text",
                                            children=[f"Region:"],
                                        ),
                                        html.P(
                                            className="card-text mb-1 fs-sm",
                                            id="team-confederation-text",
                                            children=[f"Conf: "],
                                        ),
                                        html.A(
                                            id="query-team-wiki-link",
                                            target="_blank",
                                            style={
                                                "font-size": "0.7rem"},
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

TransactionsStatsOverall = dbc.Row(
    children=[
        month_selector_card
        # participations_card,
        # matches_count_card,
    ]
)


# @callback(
#     Output("total-budget-text", "children"),
#     Input("year-select", "value"),
#     State("budget-df", "data"),
# )
# def update_team_select(query_year, budget_df):
#     df = pd.read_json(budget_df)

#     df = df.loc[(df.year == int(query_year)) & (df.category_type == 'Expense')]

#     winning_times = f'{df["amount"].sum():,.2f}'

#     return winning_times
