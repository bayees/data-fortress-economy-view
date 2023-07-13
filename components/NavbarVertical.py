from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.Div(
            [
                html.Img(src="./assets/images/navbar_icon.png", style={"width": "3rem"}),
                html.H4("Economy", className="m-0"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="tf-icons bx bx-home fas fa-home"), 
                        html.Span("Home" , className="me-2")
                    ],
                    href="/",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="tf-icons bx bx-wallet fas fa-wallet"), 
                        html.Span("Budget", className="me-2"),
                    ],
                    href="/budget",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="tf-icons bx bx-money fas fa-money"), 
                        html.Span("Actuals", className="me-2"),
                    ],
                    href="/actuals",
                    active="exact",
                    className="pe-3"
                ),
                dbc.NavLink(
                    [
                        html.I(className="tf-icons bx bx-credit-card fas fa-credit-card"), 
                        html.Span("Transaction", className="me-2"),
                    ],
                    href="/transactions",
                    active="exact",
                    className="pe-3"
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar bg-menu-theme",
)