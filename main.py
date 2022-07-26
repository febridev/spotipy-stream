import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd


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
tracks=[]
nowplaying = sp.current_user_playing_track()
current_playing_type = nowplaying['currently_playing_type']
if current_playing_type == 'episode':
    print('podcast')
    exit()
else:
    print('music')
    demo=nowplaying['item']
    tracks_name=demo['name']
    tracks_id=demo['id']
    tracks_popularity=demo['popularity']
    tracks_playing=nowplaying['timestamp']
    print(tracks_name+'-'+str(tracks_popularity))
# for lsitem in nowplaying['item']:
#     song_id = lsitem['']
# print(nowplaying['item',[row]])
# df = pd.DataFrame(nowplaying[item])

# print(df)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

# print(results)
# print(clientsecret)