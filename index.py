# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app, server

import plotly.express as px

from pages.index import index_page
from pages.not_found import not_found_page
from pages.search import search_page
from pages.insights import insights_page
from pages.artists_insights import artists_insights_page

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(
        id="page-content",
        style={
            'margin': '25px',
        },
    ),
])

app.validation_layout = html.Div([
    index_page,
    search_page,
    not_found_page,
])


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):

    if pathname == "/":
        return index_page
    elif pathname == "/search":
        return search_page
    elif pathname == "/insights":
        return insights_page
    elif pathname == "/artists_insights":
        return artists_insights_page
    else:
        return not_found_page


if __name__ == "__main__":
    app.run_server(debug=False)
