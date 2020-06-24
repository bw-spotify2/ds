#model_data/model.py

import pickle
import pandas as pd
from scipy.spatial import distance

def predict(song_attributes):
  """
  Need to pass in a variable that is an array with the below song attributes 
  in order.
  [[popularity, acousticness, danceability, duration_ms, energy, instrumentalness,
  liveness, loudness, speechiness, tempo, valence]]
  """

  df =  pd.DataFrame(song_attributes)

  ### Scale Input ###

  # import the pickled scaler model
  pickle_filename_1 = 'data\scaler_model.pkl'
  scaler_pkl = open(pickle_filename_1, 'rb')
  scaler = pickle.load(scaler_pkl) 

   # scale the input data
  input_scaled = scaler.transform(df)

  ### Encode Input ###

  # Loading the pickled autoencoder model
  pickle_filename = 'data\autoencoder_model.pkl'
    
  autoencoder_pkl = open(pickle_filename, 'rb')
  autoencoder = pickle.load(autoencoder_pkl)
  # encode the input data and set to variable
  input_x_y = (autoencoder.predict(input_scaled)[0][0], 
               autoencoder.predict(input_scaled)[0][1])

  # ### Read in the CSV ###
  database = pd.read_csv('data\encoded_data.csv')

  ### Get distances ###
  def get_e_dist(my_df):
    return distance.euclidean(my_df[[0,1]], input_x_y)

  database['e_distance'] = database.apply(get_e_dist, axis=1)

  five_smallest = database[['e_distance','track_id']].nsmallest(5, columns='e_distance', keep='all')

  five_closest = five_smallest['track_id']

  return five_closest.to_json()