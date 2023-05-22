from dash import html
import dash_bootstrap_components as dbc
from components.MapCard import MapCard

map_page_content = html.Div([
    dbc.Row([
            MapCard,
            ]),

    dbc.Row([

    ]),
], style={"padding-top": "0px"})
