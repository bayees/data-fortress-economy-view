from dash import html
import dash_bootstrap_components as dbc
from components.IntroCard import IntroCard

home_page_content = html.Div([
    dbc.Row([
            IntroCard,
            ]),

    dbc.Row([

    ]),
], style={"padding-top": "0px"})
