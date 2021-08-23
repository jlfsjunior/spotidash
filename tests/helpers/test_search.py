from helpers.search import get_search

def test_helpers001_get_search():

    s = get_search("the beatles", type_str="artist")

    assert type(s) == list, "Search did not return a list"
    assert len(s) > 0, "Search returned an empty list"

def test_helpers002_get_search_item():

    s = get_search("the beatles", type_str="artist")
    s0 = s[0]

    assert type(s0) == dict, "Search first item did not return a dict"
    assert "name" in s0.keys(), "Search first item does not have 'name' key"
