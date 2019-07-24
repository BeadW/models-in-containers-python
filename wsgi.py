# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np

# API definition
application = Flask(__name__)


@application.route("/")
def index():
    return "Hello, World!"


@application.route('/predict', methods=['POST'])
def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first.')
        return ('No model here to use')


lr = joblib.load("model.pkl") # Load "model.pkl"
print ('Model loaded')
model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
print ('Model columns loaded')


if __name__ == '__main__':

    application.run()