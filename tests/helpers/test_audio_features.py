import pandas as pd

from helpers.audio_features import get_track_df

def test_helpers001_get_track_df():
    track_df = get_track_df("the beatles")

    assert type(track_df) == pd.DataFrame, "get_track_df did not return Pandas dataframe"