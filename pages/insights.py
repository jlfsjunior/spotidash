import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table 
from dash.dependencies import Input, Output

from helpers.audio_features import get_track_df

from app import app

insights_page = html.Div(
    children=[
        dbc.Row(
            dbc.Col(
                html.H1(children="Track insights"),
                width={
                    'size': 'auto'
                },
            ),
            justify='center',
            style={
                'margin': '25px',
            }
        ),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='artist-dropdown',
                    options=[
                        {"label": "Metallica", "value": "metallica"},
                        {"label": "Daft Punk", "value": "daft punk"},
                        {"label": "Drake", "value": "drake"},
                        {"label": "Kanye West", "value": "kanye west"},
                        {"label": "Backstreet Boys", "value": "backstreet boys"},
                    ],
                    value="metallica",
                    searchable=True,
                ),
                width=4
            ),
            dbc.Col(
                dbc.FormGroup(
                    [       
                        dbc.Checkbox(
                            id="sortby-checkbox",
                            checked=False,
                            className="form-check-label",
                        ),
                        dbc.Label(
                            "Ascending",
                            html_for="sortby-checkbox",
                            className="form-check-label",
                        ),
                    ],
                    check=False,
                ),
                width=4,
            ),
            dbc.Col(
                dbc.RadioItems(
                    id='sortby-radio',
                    options=[
                        {"label": "danceability", "value": "danceability"},
                        {"label": "energy", "value": "energy"},
                        {"label": "loudness", "value": "loudness"},
                        {"label": "speechiness", "value": "speechiness"},
                        {"label": "acousticness", "value": "acousticness"},
                        {"label": "instrumentalness", "value": "instrumentalness"},
                        {"label": "liveness", "value": "liveness"},
                        {"label": "valence", "value": "valence"},
                        {"label": "tempo", "value": "tempo"},
                    ],
                    value="danceability",
                    inline=True,
                ),
                width=4
            ),
        ]),
        dbc.Row(
            dbc.Col(
                dash_table.DataTable(
                    id="insights-table",
                    # columns=[{"name": i, "id": i} for i in get_track_df("Metallica").columns],
                    # data=get_track_df("Metallica").to_dict("rows"),
                )
            )
        ),
    ]
)

@app.callback(
    [
        Output("insights-table", "data"),
        Output("insights-table", "columns"),
    ],
    [
        Input("artist-dropdown", "value"),
        Input("sortby-radio", "value"),
        Input("sortby-checkbox", "checked")
    ]
)
def update_insights_table(artist, sortby, ascending):

    if artist is None:
        artist = "Metallica"

    df = ( get_track_df(artist)
        .sort_values(sortby, ascending=ascending)
        .drop_duplicates(
            subset=["name", "duration_ms"],
            keep="last",
        )
    )

    # cols = [{"name": i, "id": i} for i in df.columns]
    cols = [
        {"name": "name", "id": "name"},
        {"name": "danceability", "id": "danceability"},
        {"name": "energy", "id": "energy"},
        {"name": "loudness", "id": "loudness"},
        {"name": "speechiness", "id": "speechiness"},
        {"name": "acousticness", "id": "acousticness"},
        {"name": "instrumentalness", "id": "instrumentalness"},
        {"name": "liveness", "id": "liveness"},
        {"name": "valence", "id": "valence"},
        {"name": "tempo", "id": "tempo"},
    ]

    return df.to_dict("records"), cols
