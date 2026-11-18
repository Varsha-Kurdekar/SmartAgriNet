from flask import Blueprint, render_template, request
from plant_disease_detection.predict import predict_disease

disease_page = Blueprint(
    'disease_page',
    __name__,
    template_folder='templates'
)

# Open Disease Page
@disease_page.route('/disease')
def disease():
    return render_template('disease.html')


# Prediction Route
@disease_page.route('/predict', methods=['POST'])
def predict():

    if 'image' not in request.files:
        return "No image uploaded"

    image = request.files['image']

    result = predict_disease(image)

    return render_template(
        'disease.html',
        prediction=result
    )