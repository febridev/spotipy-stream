import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import threading
from kafka import KafkaConsumer
from json import loads
import time

consumer = KafkaConsumer(
    'week6_demo',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

while(True):
    for message in consumer:
        message = message.value
        print(message)
    time.sleep(5)