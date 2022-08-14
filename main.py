import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import threading
from kafka import KafkaProducer
from json import dumps
import time

def get_current_play():        
    clientid = '751673d086fa4c6d9d764cc4a3cfcf7d'
    clientsecret = '82e0acf2df9244efb2781e261f0e0e94'
    redirect = 'http://localhost/callback'
    scope='user-read-recently-played user-read-currently-playing playlist-modify-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientid,
                                                client_secret=clientsecret,
                                                redirect_uri=redirect,
                                                # open_browser=None,
                                                scope=scope))

    tracks=[]
    nowplaying = sp.current_user_playing_track()
    np = nowplaying["item"]
    title = np["name"]
    popular = np["popularity"]
    timeplay = nowplaying["timestamp"]
    listss = {'title':title, 'popular':popular, 'timeplay':timeplay}
    tracks.append(listss)
    producer.send('week6_demo', value=tracks)
    producer.flush()
    print(tracks)

# get_current_play()
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
while True:
    threading.Thread(target=get_current_play).start()
    time.sleep(5)