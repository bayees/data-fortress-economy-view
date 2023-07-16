import sys
import os

module_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
if module_path not in sys.path:
    sys.path.append(module_path)

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
import pandas as pd
from components.NavbarVertical import sidebar
from components.Footer import Footer
from dash.dependencies import Input, Output
from pages.home import home_page_content
from pages.budget import budget_page_content
from pages.actuals import actuals_page_content
from pages.transactions import transactions_page_content
import glob
from utils.data import get_budget, get_actuals


# RAW
ROOT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__))))
SRC_FOLDER = os.path.join(ROOT_FOLDER, "/")
ASSETS_FOLDER = os.path.join(SRC_FOLDER, "assets/")

# Processed
budget_df = get_budget()
actuals_df = get_actuals()

# Data Store for all the dataframes used in the app to avoid reading from server. Data is stored client side in JSON format.
data_store = html.Div(
    [
        dcc.Store(id="budget-df", data=budget_df.to_json(date_format = 'iso')),
        dcc.Store(id="actuals-df", data=actuals_df.to_json(date_format = 'iso')),
    ]
)

external_style_sheet = glob.glob(
    os.path.join(ASSETS_FOLDER, "bootstrap/css") + "/*.css"
)
external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER, "css") + "/*.css")
external_style_sheet += glob.glob(os.path.join(ASSETS_FOLDER, "fonts") + "/*.css")

app = dash.Dash(
    __name__,
    title="Economy Dashboard",
    external_stylesheets=[dbc.themes.BOOTSTRAP] + external_style_sheet,
    suppress_callback_exceptions=True,
)

server = app.server

def serve_layout():
    return html.Div(
        className="layout-wrapper layout-content-navbar",
        children=[
            html.Div(
                className="layout-container",
                children=[
                    dcc.Location(id="url"),
                    data_store,
                    html.Aside(className="", children=[sidebar]),
                    html.Div(
                        className="layout-page",
                        children=[
                            html.Div(
                                className="content-wrapper",
                                children=[
                                    html.Div(
                                        className="flex-grow-1 container-p-y p-0",
                                        id="page-content",
                                        children=[],
                                    ),
                                    html.Footer(
                                        className="content-footer footer bg-footer-theme",
                                        children=[Footer],
                                        style={"margin-left": "6rem"},
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
            )
        ],
    )

app.layout = serve_layout

@callback(
    Output(component_id="page-content", component_property="children"),
    Input(component_id="url", component_property="pathname"),
)
def routing(path):
    if path == "/":
        return home_page_content
    elif path == "/budget":
        return budget_page_content
    elif path == "/actuals":
        return actuals_page_content
    elif path == "/transactions":
        return transactions_page_content


app.index_string = """<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
"""

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=5050, debug=True)
