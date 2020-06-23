from flask import Flask
from flask import request

import json
import requests
import math

# TODO: Load model

APP = Flask(__name__)

@APP.route('/')
def root():
    # song_id = request.args.get('song_id')
    return "This works"
    # return get_song_recommendations(song_id)

@APP.route('/song')
def get_recommendations():
    song_id = request.args.get('song_id')
    return get_song_recommendations(song_id)

def get_song_recommendations(song_id):
    # TODO: send song id to model
    return {'data': [{
        'id': '7qiZfU4dY1lWllzX7mPBI',
        'name': 'Shape of You',
        'artists': 'Ed Sheeran',
        'danceability': 0.825,
        'energy': 0.652,
        'key': 1.0,
        'loudness': -3.183,
        'mode': 0.0,
        'speechiness': 0.0802,
        'acousticness': 0.581000,
        'instrumentalness': 0.000000,
        'liveness': 0.0931,
        'valence': 0.9310,
        'tempo': 95.977,
        'duration_ms': 233713.0,
        'time_signature': 4.0
    },{
        'id': '5CtI0qwDJkDQGwXD1H1cL',
        'name': 'Despacito - Remix',
        'artists': 'Luis Fonsi',
        'danceability': 0.694,
        'energy': 0.815,
        'key': 2.0,
        'loudness': -4.328,
        'mode': 1.0,
        'speechiness': 0.1200,
        'acousticness': 0.229000,
        'instrumentalness': 0.000000,
        'liveness': 0.0924,
        'valence': 0.8130,
        'tempo': 88.931,
        'duration_ms': 228827.0,
        'time_signature': 4.0
    }]}








