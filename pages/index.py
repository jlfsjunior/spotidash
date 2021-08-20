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
    ]
)