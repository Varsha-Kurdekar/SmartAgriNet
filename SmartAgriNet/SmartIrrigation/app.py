from flask import Blueprint, render_template, request, jsonify
import pickle
import pandas as pd

irrigation_page = Blueprint(
    'irrigation_page',
    __name__,
    template_folder='templates'
)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, 'model.pkl')

model = pickle.load(open(model_path, 'rb'))

@irrigation_page.route('/irrigation', methods=['GET', 'POST'])
def irrigation():

    if request.method == 'POST':

        data = request.get_json()

        print("JSON DATA:", data)

        temperature = data['temperature']
        humidity = data['humidity']
        soil_moisture = data['soil_moisture']
        rainfall = data['rainfall']

        input_data = pd.DataFrame([{
            'temperature': temperature,
            'humidity': humidity,
            'soil_moisture': soil_moisture,
            'rainfall': rainfall
        }])

        print("Input Data:")
        print(input_data)

        prediction = model.predict(input_data)

        print("Prediction:", prediction)

        return jsonify({
            'irrigation': int(prediction[0])
        })

    return render_template('irrigation.html')