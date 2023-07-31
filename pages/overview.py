from dash import html
import dash_bootstrap_components as dbc
from components.BalanceChartCard import balance_chart_card

overview_page_content = html.Div(
    children=[
        dbc.Row(
            children=[
                balance_chart_card,
            ],
        ),
        dbc.Row(
        ),
        dbc.Row(
        ),
    ],
    style={"padding-top": "0rem"},
)
