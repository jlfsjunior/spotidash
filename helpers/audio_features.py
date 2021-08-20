import pandas as pd

from .spotify import spotify

def get_track_df(artist_query):
    res = spotify.search(q="artist:" + artist_query, type='track', limit = 50)
    tracks = res['tracks']['items']

    track_info_df = pd.DataFrame([ {
        "id": t["id"],
        "name": t["name"],
        "disc_number": t["disc_number"],
        "explicit": t["explicit"],
    } for t in tracks]).set_index("id")

    res = spotify.audio_features(track_info_df.index)
    track_audio_feat_df = pd.DataFrame(res).set_index("id")

    track_df = pd.merge(
        track_info_df, 
        track_audio_feat_df, 
        left_index=True, 
        right_index=True
    )

    return track_df


