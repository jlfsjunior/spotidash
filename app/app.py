# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.express as px

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import configparser

config = configparser.ConfigParser()
config.read("app.cfg")

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=config["default"]["ClientID"],
        client_secret=config["default"]["ClientSecret"],
        # scope='user-library-read',
    )
)

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

def get_search(search_term, type_str="artist"):

    results = spotify.search(q=type_str + ":" + search_term, type=type_str)

    print(results)

    items = results[type_str + "s"]["items"]

    items = [
        {
            "name": i["name"],
            "popularity": i["popularity"],
            "image": _get_image(i),
            "artist": _get_artist(i),
            "url": _get_url(i),
        }
        for i in items
    ]

    return items


def _get_image(item):
    if "images" in item:
        if len(item["images"]) > 0:
            return item["images"][0]["url"]
        else:
            return ""
    else:
        return ""


def _get_artist(item):
    if "artists" in item:
        if len(item["artists"]) > 0:
            return item["artists"][0]["name"]
        else:
            return ""
    else:
        return ""

def _get_url(item):
    if "external_urls" in item:
        return item['external_urls']['spotify']


app.layout = html.Div(
    children=[
        dbc.Row(
            dbc.Col(
                html.H1(children="Hello Spotidash!"),
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
                html.Div(
                    [
                        dcc.Textarea(
                            id="textarea", 
                            style={"width": "100%"},
                        ),
                        dbc.RadioItems(
                            id="radio",
                            options=[
                                {"label": "Artist", "value": "artist"},
                                {"label": "Track", "value": "track"},
                                {"label": "Album", "value": "album"},
                                {"label": "Show", "value": "show"},
                                {"label": "Playlist", "value": "playlist"},
                                {"label": "Episode", "value": "episode"},
                            ],
                            value="artist",
                            inline=True,
                            style={"width": "100%"},
                        ),
                    ]
                ),
                width = {
                    'size': 6,
                    'offset': 3,
                }
            ),
        ),

        dbc.Row(
            dbc.Col(
                dbc.CardDeck(id="test"),
            ),
        ),
    ],
    style={
        'margin': '0 25px',
    }
)


def make_card(item):

    print(item)

    if "artists" in item:
        txt = "Artist: " + item["artists"][0]["name"]
    else:
        txt = ""

    return dbc.Card(
        [
            dbc.CardImg(src=item["image"], top=True),
            dbc.CardBody(
                [
                    html.H4(item["name"], className="card-title"),
                    html.A(
                        item["name"],
                        href=item["url"],
                        target="_blank",
                    ),
                    html.P(
                        [
                            f"Popularity: {item['popularity']}",
                            txt,
                        ],
                        className="card-text",
                    ),
                ]
            ),
        ],
        color="dark",
        inverse=True,
        style={"width": "18rem"},
    )


@app.callback(
    Output("test", "children"),
    Input("textarea", "value"),
    Input("radio", "value"),
)
def update_output(text, type_str):

    if text is None:
        return "Please type something..."

    val = get_search(text, type_str=type_str)

    return [make_card(i) for i in val]


if __name__ == "__main__":
    app.run_server(debug=False)
