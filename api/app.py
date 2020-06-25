from flask import Flask
from flask import request

import json, jsonify
import requests, math
from model import predict

app = Flask(__name__)

@app.route('/', methods = ["POST"])
def root():
    return request.get_json()
    # return get_song_recommendations(song_id)

@app.route('/song', methods = ["POST"])
def get_recommendations():
    song_id = request.args.get_json('song_id')
    return get_song_recommendations(song_id)

def get_song_recommendations(song_id):
    song_id_list = predict(song_features)
    return {song_id_list}
    

