from .spotify import spotify

def get_search(search_term, type_str="artist"):

    results = spotify.search(q=type_str + ":" + search_term, type=type_str)

    items = results[type_str + "s"]["items"]

    items = [
        {
            "name": i["name"],
            "popularity": i["popularity"],
            "image": _get_image(i),
            "artist": _get_artist(i),
            "url": _get_url(i),
        }
        for i in items
    ]

    return items


def _get_image(item):
    if "images" in item:
        if len(item["images"]) > 0:
            return item["images"][0]["url"]
        else:
            return ""
    else:
        return ""


def _get_artist(item):
    if "artists" in item:
        if len(item["artists"]) > 0:
            return item["artists"][0]["name"]
        else:
            return ""
    else:
        return ""

def _get_url(item):
    if "external_urls" in item:
        return item['external_urls']['spotify']