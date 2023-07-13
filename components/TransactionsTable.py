from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback, dash_table
from dash.dependencies import Input, Output, State

TransactionsTable = html.Div(
    className="col-md-12 col-lg-12 mb-md-0 mb-12 card-chart-container",
    children=[
        html.Div(
            className="card",
            children=[
                html.Div(
                    className="card-header card-m-0 me-2 pb-3",
                    children=[
                        html.H4(
                            "Transactions",
                            className="card-title m-0 me-2",
                            style={"font-size": "1.5vw"},
                        ),
                    ],
                ),
                html.Div(
                    className="table-responsive text-nowrap overflow-auto",
                    children=[html.Div(id="transactions-table", children=[])],
                ),
            ],
        )
    ],
)


@callback(
    Output("transactions-table", "children"),
    Input("transactions-month-select", "value"),
    State("actuals-df", "data"),
)
def update_table(query_month, actuals_df):
    df = pd.read_json(actuals_df)

    df = df.loc[(df.month == query_month)]

    df.loc[:, "amount"] = df["amount"].map("{:,.2f}".format)

    return dbc.Table.from_dataframe(
        df,
        columns=["date_actual", "category_type", "description", "category", "main_category", "amount"],
        #header=["Category", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Year Total"],
        class_name="no-footer",
        striped=False,
        bordered=False,
        hover=True,
        responsive=True,
    )
