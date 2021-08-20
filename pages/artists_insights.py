import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table 
from dash.dependencies import Input, Output

from helpers.audio_features import get_track_df

from app import app

artists_insights_page = html.Div(
    children=[
        dbc.Row(
            dbc.Col(
                html.H1(children="Artists insights"),
                width={
                    'size': 'auto'
                },
            ),
            justify='center',
            style={
                'margin': '25px',
            }
        ),
    ]
)

