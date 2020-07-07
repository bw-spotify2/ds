from flask import Flask
from flask import request

import json, jsonify
import requests, math
from model import predict

app = Flask(__name__)

@app.route('/', methods = ["POST"])
def root():
    variables = ["acousticness", "danceability", "duration_ms", "energy",
     "instrumentalness", "liveness", "loudness", "speechiness", "tempo", 
     "valence", "key", "mode", "time_signature"]
    data = request.args
    filtered_var = []
    for x in variables:
        filtered_var.append(data[x])

    return_ids = predict([filtered_var])

    return json.dumps(return_ids)

