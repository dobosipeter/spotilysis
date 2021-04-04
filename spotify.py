# using: https://spotipy.readthedocs.io/en/2.17.1/#installation

import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth


def get_top_tracks():
    scope = "user-top-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_top_tracks(limit=50)

    df = pd.DataFrame.from_dict(results['items'])

    return df


def get_top_artists():
    scope = "user-top-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_top_artists(limit=50)

    df = pd.DataFrame.from_dict(results['items'])

    return df
