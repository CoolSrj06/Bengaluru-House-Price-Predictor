from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open("./model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])
    sqft = float(data['sqft'])

    # Example input format (adjust based on your model)
    input_data = pd.DataFrame({
        'location': [location],
        'total_sqft': [sqft],
        'bath': [bath],
        'bhk': [bhk]
    })

    prediction = model.predict(input_data)[0]

    return jsonify({"price": round(prediction, 2)})

if __name__ == "__main__":
    app.run()