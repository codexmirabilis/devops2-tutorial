from flask import Flask, Response
from flask_cors import CORS
import pandas as pd
import pickle
import os

# Aufgabe 2
app = Flask(__name__)
CORS(app)

data = pd.read_csv(os.path.join('data', 'auto-mpg.csv'))
# print(data.to_json())

# Load trained model
file_to_open = open(os.path.join(
    'data', 'models', 'linear_regressor.pickle'), 'rb')
trained_model = pickle.load(file_to_open)
file_to_open.close()


@app.route("/")
def index():
    return {'hello': 'world'}


@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/training_data")
def training_data():
    return Response(data.to_json(), mimetype='application/json')
