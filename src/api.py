from flask import Flask, Response, request
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


# Aufgabe 3
@app.route("/predict", methods=['GET'])
def predict():
    zylinder = request.args.get('zylinder')
    ps = request.args.get('ps')
    gewicht = request.args.get('gewicht')
    beschleunigung = request.args.get('beschleunigung')
    baujahr = request.args.get('baujahr')

    # print(zylinder, ps, gewicht, beschleunigung, baujahr)

    df = pd.DataFrame({'zylinder': [zylinder], 'ps': [ps], 'gewicht': [gewicht],
                       'beschleunigung': [beschleunigung], 'baujahr': [baujahr]})

    print(df)

    prediction = trained_model.predict(df)
    # print(prediction)

    return {'result': prediction[0]}
    # return ''
