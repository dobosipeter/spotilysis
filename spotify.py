# using: https://spotipy.readthedocs.io/en/2.17.1/#installation

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import Counter


def get_top_tracks():
    scope = "user-top-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    result = sp.current_user_top_tracks()
    artists = []
    for item in result['items']:
        artist = item['artists'][0]['name']
        artists.append(artist)
        name = item['name']
        print(artist + " - " + name)

    alma = Counter(artists)
    alma = dict(alma)
    print(alma)
    for item in alma:
        print(item + ": " + str(alma[item]))
