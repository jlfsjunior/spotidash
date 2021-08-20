import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from helpers.search import get_search
from helpers.layout.cards import make_artist_card

from app import app

search_page = html.Div(
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

@app.callback(
    Output("test", "children"),
    Input("textarea", "value"),
    Input("radio", "value"),
)
def update_output(text, type_str):

    if text is None:
        return "Please type something..."

    val = get_search(text, type_str=type_str)

    return [make_artist_card(i) for i in val]