import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table 
from dash.dependencies import Input, Output, State

from helpers.audio_features import get_track_df
from helpers.artist import search_artist, get_related_artist

from app import app

related_artists = get_related_artist(
    search_artist('The Beatles')["id"]
)

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
        dbc.Row(
            dbc.Col(
                children=[
                    dbc.Input(
                        id="artist-input", 
                        placeholder="Enter an artist...", 
                        type="text"
                    ),
                    dbc.Button(
                        id="artist-submit",
                        children="Submit",
                        type="submit",
                        color="success",
                    ),
                ],
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div(id="related-artists-table"),
                width=12,
            )
        )
    ]
)


@app.callback(
    Output('related-artists-table', 'children'),
    Input('artist-submit', 'n_clicks'),
    State('artist-input', 'value')
)
def submit_artist(n_clicks, artist_query):

    if artist_query is None:
        return ""

    artist = search_artist(artist_query)

    related_artists = get_related_artist(artist["id"])

    re_related_artists_dfs = [ {"name": i.name, "id": i.id, "data": get_related_artist(i.id)} for i in related_artists.itertuples()]

    return [ 
        dash_table.DataTable(
            id="table",
            columns=[ {"name": i, "id": i} for i in ["id", "name", "followers", "popularity"]],
            data=related_artists.to_dict("records"),
        )
    ] + [
        html.Div(
            [
                html.H3(df_dict["name"]),
                dash_table.DataTable(
                    columns=[ {"name": i, "id": i} for i in ["id", "name", "followers", "popularity"]],
                    data=df_dict["data"].to_dict("records"),
                ),
            ]
        ) for df_dict in re_related_artists_dfs 
    ]


