import dash

import sys 
sys.path.append('.')

from index import app

def test_app001_run(dash_duo):

    dash_duo.start_server(app)

    print(dash_duo.server_url)

    assert True, "Boilerplate"

