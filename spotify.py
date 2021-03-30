# using: https://spotipy.readthedocs.io/en/2.17.1/#installation

import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_top_tracks():
    scope = "user-top-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    result = sp.current_user_top_tracks()
    for item in result['items']:
        artist = item['artists'][0]['name']
        name = item['name']
        print(artist + " - " + name)
