import dash

import sys 
sys.path.append('.')

from index import app

def test_app001_run(dash_duo):

    dash_duo.start_server(app)

    print(dash_duo.server_url)

    assert True, "Boilerplate"

def test_app002_load_search(dash_duo):

    dash_duo.start_server(app)

    dash_duo.wait_for_page(dash_duo.server_url + '/search', timeout=5)

    assert dash_duo.get_url() == dash_duo.server_url + '/search', "Page not loaded"
