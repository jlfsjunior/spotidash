from .spotify import spotify
import pandas as pd

def _parse_artist(item):

    return {
        'id' : item['id'],
        'name' : item['name'],
        'genres' : item['genres'],
        'popularity' : item['popularity'],
        'followers' : item['followers']['total'],
        'url': item['external_urls']['spotify'],
        'image': item['images'][0]['url'],
    }

def _parse_track(item):

    return {
        'id' : item['id'],
        'name' : item['name'],
        'popularity' : item['popularity'],
        'followers' : item['followers']['total'],
        'duration_ms' : item['duration_ms'],
        'explicit' : item['explicit'],
        'url': item['external_urls']['spotify'],
        'image': item['images'][0]['url'],
    }

def get_related_artist(artist_id):
        
    res = spotify.artist_related_artists(artist_id)
    
    related_artists = res['artists']
    related_artists = [ _parse_artist(i) for i in related_artists]

    df = pd.DataFrame(related_artists)

    return df

def get_top_tracks(artist_id, country = "US"):

    res = spotify.artist_top_tracks(artist_id, country)

    res = [ _parse_track(i) for i in res]

    df = pd.DataFrame(res)

    return df

def search_artist(search_term):

    artist_keys = ['id', 'name', 'genres', 'popularity', 'followers']

    res = spotify.search("artist:" + search_term, type = 'artist')

    artist = res['artists']['items'][0]    

    return _parse_artist(artist)