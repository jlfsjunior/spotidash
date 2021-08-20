import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import os

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET')
        # scope='user-library-read',
    )
)
