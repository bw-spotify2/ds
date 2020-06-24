from flask import Flask
from flask import request

import json, jsonify
import requests, math

# TODO: Load model (model_data model.py)

app = Flask(__name__)

@app.route('/')
def root():
    # song_id = request.args.get('song_id')
    return "This works"
    # return get_song_recommendations(song_id)

@app.route('/song')
def get_recommendations():
    song_id = request.args.get('song_id')
    return get_song_recommendations(song_id)

def get_song_recommendations(song_id):
    # TODO: send song id to model
    return {song_id_list}
