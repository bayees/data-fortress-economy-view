import plotly.express as px
import pandas as pd
from dash import html, dcc
import utils.theme as theme
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls
from dash import callback

ExpensePerCategory = html.Div(className="card-chart-container col-lg-12 md-12 sm-12",
                       children=[
                           html.Div(
                               className="card-chart",
                               children=[
                                   html.H4("Expense per category",
                                           className="card-header card-m-0 me-2 pb-3", style={"font-size": "1.5vw"}),
                                   html.Div(
                                       id="expense-per-category",
                                       children=[


                                       ]
                                   )
                               ]
                           )

                       ],
                       style={"min-height" :"26.25rem"}
                       )


@callback(
    Output("expense-per-category", "children"),
    Input("month-select", "value"),
    State("actuals-df" , "data")
)
def update_figures(query_month, actuals_data):
    actuals_df = pd.read_json(actuals_data)

    actuals_df = actuals_df.loc[(actuals_df.month == query_month) & (actuals_df.category_type == "Expense")]
    
    actuals_df['amount_actual'] = actuals_df['amount'].abs()

    fig_category = px.bar(actuals_df.groupby(['category'])['amount_actual'].sum().reset_index().sort_values(by='amount_actual', ascending=False), x='category',
                 y='amount_actual', template='simple_white')
    
    fig_category.update_layout(
        xaxis=dict(
            tickangle=45,
            type='category',
            title='Category',
            titlefont_size=16,
            tickfont_size=14,
        ),
        yaxis=dict(
            title='Amount',
            titlefont_size=16,
            tickfont_size=14,
        ),
    )

    fig_category.update_traces(marker_color='#349934')

    return dcc.Graph(figure=fig_category)
    #     update_xaxes(type="category")
    #     .update_layout(paper_bgcolor="rgb(0,0,0,0)",
    #                    plot_bgcolor="rgb(0,0,0,0)",
    #                    legend=dict(
    #                        bgcolor=theme.LEGEN_BG),
    #                    font_family=theme.FONT_FAMILY,
    #                    ),
    #     config={
    #     "displayModeBar": False},
    #     style=theme.CHART_STYLE

    # )