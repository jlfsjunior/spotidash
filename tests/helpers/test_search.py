from helpers.search import get_search

get_search(search_term, type_str="artist")

def test_helpers001_get_search():

    s = get_search("the beatles", type_str="artist")

    assert type(s) == "list", "Search did not return a list"
    assert len(s) > 0, "Search returned an empty list"
