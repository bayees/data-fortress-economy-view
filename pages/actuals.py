from dash import html
import dash_bootstrap_components as dbc
from components.ActualsStatsOverall import ActualsStatsOverall
from components.ExpensesPerCategory import ExpensePerCategory
from components.DifferencePerCategory import DifferencePerCategory

actuals_page_content = html.Div(
    children=[
        dbc.Row(
            ActualsStatsOverall
        ),
        dbc.Row(
            DifferencePerCategory
        ),
        dbc.Row(
            ExpensePerCategory
        ),
    ],
    style={"padding-top": "0rem"},
)
