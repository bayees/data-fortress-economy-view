from dash import html
import dash_bootstrap_components as dbc

IntroCard = html.Div(
    className="col-md-12 col-lg-12 mb-md-0 mb-4 card-chart-container",
    children=[
        html.Div(
            className="card",
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            className="col-lg-6",
                            children=[
                                html.Div(
                                    className="card-header card-m-0 me-2 pb-3",
                                    children=[
                                        html.H2(
                                            ["Personal finance Dashboard"],
                                            className="card-title m-0 me-2 mb-2",
                                            style={"font-size": "2vw"},
                                        ),
                                        html.Span(
                                            "From Data Science Point-of-View",
                                            style={
                                                "color": "#0084d6",
                                                "font-size": "1.5vw",
                                            },
                                        ),
                                    ],
                                ),
                                html.P(
                                    [
                                        "A personal budget dashboard is a visual representation of an individual's spending habits and financial goals. The dashboard shows the user's estimated expenses and income for a certain period, along with their actual spending and earnings. This allows users to track their expenses against their budget in real-time and make informed decisions about future purchases.",
                                        html.A(
                                            " Budget tab.",
                                            href="/budget",
                                            style={"color": "#0084d6"},
                                        ),
                                    ],
                                    className="card-title me-4",
                                ),
                                html.P(
                                    [
                                        "The dashboard typically includes various charts and graphs that display key financial metrics such as monthly income, expenses by category, and changes in net worth over time. Users can drill down into specific categories of expenses to see where they are overspending and adjust their budgets accordingly.",
                                    ],
                                    className="card-title me-4",
                                ),
                                html.P(
                                    [
                                        "The personal budget dashboard can be customized to include specific features such as alerts when a user exceeds their budget or reminders to pay bills on time. It can also integrate with personal finance software or bank accounts to automatically import spending data and simplify tracking expenses.",
                                    ],
                                    className="card-title me-4",
                                ),
                                html.P(
                                    [
                                        "Overall, a personal budget dashboard provides users with a comprehensive view of their finances and helps them stay on top of their spending and saving goals.",
                                    ],
                                    className="card-title me-4",
                                ),
                            ],
                        ),
                    ]
                ),
            ],
        )
    ],
)
