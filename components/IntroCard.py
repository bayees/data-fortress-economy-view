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
                                            ["Personal Location Tracking"],
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
                                        "A personal location tracking dashboard is a visual representation of an individual's movements and travel history. The dashboard shows the user's estimated location and route for a certain period, along with their actual location and travel history. This allows users to track their movements against their plans in real-time and make informed decisions about future travel.",
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
                                        "The location tracking dashboard can be customized to include specific features such as alerts when a user deviates from their planned route or reminders to visit certain locations on time. It can also integrate with travel planning software or transportation accounts to automatically import travel data and simplify tracking movements.",
                                    ],
                                    className="card-title me-4",
                                ),
                                html.P(
                                    [
                                        "The location tracking dashboard can be customized to include specific features such as alerts when a user deviates from their planned route or reminders to visit certain locations on time. It can also integrate with travel planning software or transportation accounts to automatically import travel data and simplify tracking movements.",
                                    ],
                                    className="card-title me-4",
                                ),
                                html.P(
                                    [
                                        "Overall, a location tracking dashboard provides users with a comprehensive view of their movements and helps them stay on top of their travel plans and goals.",
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
