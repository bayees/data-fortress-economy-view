from dash import html
import dash_bootstrap_components as dbc
from utils.consts import actuals
from dash.dependencies import Input, Output, State
from dash import callback
import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc

balance_chart_card = html.Div(className="card-chart-container col-lg-12 md-12 sm-12",
                       children=[
                           html.Div(
                               className="card-chart",
                               children=[
                                   html.H4("Expense per category",
                                           className="card-header card-m-0 me-2 pb-3", style={"font-size": "1.5vw"}),
                                   html.Div(
                                       id="overview",
                                       children=[
                                       ]
                                   )
                               ]
                           )

                       ],
                       style={"min-height" :"26.25rem"}
                       )


@callback(
    Output("overview", "children"),
    Input(component_id="url", component_property="pathname"),
    State("actuals-df" , "data")
)
def update_figures(query_month, actuals_data):
    actuals_df = pd.read_json(actuals_data)

    actuals_df = actuals_df.loc[(actuals_df.date_actual >= '2022-08-01')]

    # https://www.statology.org/pandas-pivot-table-sum/
    sum_catagory_type_df = pd.pivot_table(actuals_df, values='amount', index='month', columns='category_type', aggfunc='sum')

    # https://stackoverflow.com/questions/54908602/getting-the-latest-value-from-a-group-in-pandas
    period_balance_df = actuals_df.sort_values(by=['date_actual']).groupby('month')[['balance', 'amount']].agg({'balance':'last'}).reindex(actuals_df['month'].unique(), fill_value=0).reset_index()

    merge_df = pd.merge(sum_catagory_type_df[['Income', 'Expense']], period_balance_df, on="month")

    #actuals_df = actuals_df.loc[(actuals_df.month == query_month) & (actuals_df.category_type == "Expense")]
    
    #actuals_df['amount_actual'] = actuals_df['amount'].abs()

    data = [
        go.Bar(
            x=merge_df['month'], # assign x as the dataframe column 'x'
            y=merge_df['Income'],
            marker_color='#7ac27a',
            name='Income',
        ),
        go.Bar(
            x=merge_df['month'],
            y=merge_df['Expense'].abs(),
            marker_color='#FF726E',
            name='Expense',
        ),
        go.Scatter(
            x=merge_df['month'],
            y=merge_df['balance'],
            marker_color='#000',
            name='Balance',
        )

    ]

    layout = go.Layout(
        barmode='group',
        margin=dict(l=40, r=50, t=0, b=40),
        plot_bgcolor = "white",
        yaxis=dict(
            gridcolor="grey",
            showgrid=True,
            zeroline=True, 
            zerolinewidth=1,
            zerolinecolor='grey',
            gridwidth=1,
        ),
    )
    

    fig = go.Figure(data=data, layout=layout)


    return dcc.Graph(figure=fig)