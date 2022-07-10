import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth


clientid = '751673d086fa4c6d9d764cc4a3cfcf7d'
clientsecret = '82e0acf2df9244efb2781e261f0e0e94'
redirect = 'http://localhost'
scope='user-read-recently-played user-read-currently-playing playlist-modify-private'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientid,
                                                client_secret=clientsecret,
                                                redirect_uri=redirect,
                                                scope=scope))
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clientid,
#                                                            client_secret=clientsecret))

results = sp.current_user_playing_track()

# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

print(results)
# print(clientsecret)