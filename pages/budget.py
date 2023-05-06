from dash import html
import dash_bootstrap_components as dbc
from components.BudgetTable import BudgetTable
from components.BudgetStatsOverall import BudgetStatsOverall

budget_page_content = html.Div(
    children=[
        dbc.Row(
            BudgetStatsOverall
        ),
        dbc.Row(
            children=[
                BudgetTable
            ]
        ),
    ],
    style={"padding-top": "0rem"},
)

