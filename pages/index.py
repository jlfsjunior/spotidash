import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

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
            dbc.Col(
                [
                    dcc.Link("Home", href="/"),
                    dcc.Link("Search", href="/search"),
                    dcc.Link("Track Insights", href="/insights"),
                    dcc.Link("Artists Insights", href="/artists-insights"),
                ]
            ),
            justify='center',
        )
    ]
)