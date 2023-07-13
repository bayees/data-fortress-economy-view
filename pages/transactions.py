from dash import html
import dash_bootstrap_components as dbc
from components.TransactionsTable import TransactionsTable
from components.TransactionsStatsOverall import TransactionsStatsOverall

transactions_page_content = html.Div(
    children=[
        dbc.Row(
            children=[
                TransactionsStatsOverall
            ]
        ),
        dbc.Row(
            children=[
                TransactionsTable
            ]
        ),
    ],
    style={"padding-top": "0rem"},
)

