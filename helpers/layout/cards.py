import dash_html_components as html
import dash_bootstrap_components as dbc

def make_artist_card(item):

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


def make_album_card(item):

    if "artists" in item:
        txt = "Artist: " + item["artists"][0]["name"]
    else:
        txt = ""

    return dbc.Card(
        [
            dbc.CardImg(src=item['images'][0]['url'], top=True),
            dbc.CardBody(
                [
                    html.H4(item["name"], className="card-title"),
                    html.A(
                        item["name"],
                        href=item["external_urls"]["spotify"],
                        target="_blank",
                    ),
                    html.P(
                        [
                            txt
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