import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

page_list = [
    {"title": "Home", "href": "/"},
    {"title": "Search", "href": "/search"},
    {"title": "Track Insights", "href": "/insights"},
    {"title": "Artists Insights", "href": "/artists-insights"},
]

index_page = html.Div(
    children=[
        dbc.Row(
            dbc.Col(
                html.H1(children="Hello Spotidash!"),
                width={
                    'size': 'auto'
                },
            ),
            justify='center',
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Link(page["title"], href=page["href"])
                ) for page in page_list
            ],
            justify='between',
        )
    ]
)