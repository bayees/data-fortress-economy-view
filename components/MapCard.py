from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc
import numpy as np
import plotly.express as px

MapCard = html.Div(
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
                                dcc.Graph(id='plot'),
                            ],
                        ),
                    ]
                ),
            ],
        )
    ],
)

# Define the callback functions
@app.callback(
    Output('plot', 'figure'),
    Input('category-dropdown', 'value'),
    Input('date-range-picker', 'start_date'),
    Input('date-range-picker', 'end_date')
)
def update_plot(selected_location, start_date, end_date):
    # Filter the data based on the selected category and date range
    filtered_df = df[(df['location_of_interest'] == selected_location) | (
        selected_location == 'All')]
    filtered_df = filtered_df[(filtered_df['date_actual'] >= start_date) & (
        filtered_df['date_actual'] <= end_date)]

    zoom, center = _zoom_center(
        lons=filtered_df['longitude'],
        lats=filtered_df['latitude']
    )
    # Create the plot
    fig = px.density_mapbox(filtered_df, lat='latitude', lon='longitude', radius=10,
                            center=center, zoom=zoom, height=900)
    fig.update_layout(mapbox_style="light", mapbox_accesstoken=token)


    return fig


def _zoom_center(lons: tuple=None, lats: tuple=None, lonlats: tuple=None,
        format: str='lonlat', projection: str='mercator',
        width_to_height: float=2.0) -> (float, dict):
    """Finds optimal zoom and centering for a plotly mapbox.
    Must be passed (lons & lats) or lonlats.
    Temporary solution awaiting official implementation, see:
    https://github.com/plotly/plotly.js/issues/3434
    
    Parameters
    --------
    lons: tuple, optional, longitude component of each location
    lats: tuple, optional, latitude component of each location
    lonlats: tuple, optional, gps locations
    format: str, specifying the order of longitud and latitude dimensions,
        expected values: 'lonlat' or 'latlon', only used if passed lonlats
    projection: str, only accepting 'mercator' at the moment,
        raises `NotImplementedError` if other is passed
    width_to_height: float, expected ratio of final graph's with to height,
        used to select the constrained axis.
    
    Returns
    --------
    zoom: float, from 1 to 20
    center: dict, gps position with 'lon' and 'lat' keys

    >>> print(zoom_center((-109.031387, -103.385460),
    ...     (25.587101, 31.784620)))
    (5.75, {'lon': -106.208423, 'lat': 28.685861})
    """
    if lons is None and lats is None:
        if isinstance(lonlats, tuple):
            lons, lats = zip(*lonlats)
        else:
            raise ValueError(
                'Must pass lons & lats or lonlats'
            )
    
    maxlon, minlon = max(lons), min(lons)
    maxlat, minlat = max(lats), min(lats)
    center = {
        'lon': round((maxlon + minlon) / 2, 6),
        'lat': round((maxlat + minlat) / 2, 6)
    }
    
    # longitudinal range by zoom level (20 to 1)
    # in degrees, if centered at equator
    lon_zoom_range = np.array([
        0.0007, 0.0014, 0.003, 0.006, 0.012, 0.024, 0.048, 0.096,
        0.192, 0.3712, 0.768, 1.536, 3.072, 6.144, 11.8784, 23.7568,
        47.5136, 98.304, 190.0544, 360.0
    ])
    
    if projection == 'mercator':
        margin = 1.2
        height = (maxlat - minlat) * margin * width_to_height
        width = (maxlon - minlon) * margin
        lon_zoom = np.interp(width , lon_zoom_range, range(20, 0, -1))
        lat_zoom = np.interp(height, lon_zoom_range, range(20, 0, -1))
        zoom = round(min(lon_zoom, lat_zoom), 2) - 0.3
    else:
        raise NotImplementedError(
            f'{projection} projection is not implemented'
        )
    
    return zoom, center