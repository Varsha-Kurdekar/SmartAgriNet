from flask import Flask, render_template

# IMPORT BLUEPRINTS
from SmartIrrigation.app import irrigation_page
from plant_disease_detection.app import disease_page
from agriguard.app import agriguard_page
from Weather.app import weather_page

# CREATE APP
app = Flask(__name__)

# REGISTER BLUEPRINTS
app.register_blueprint(irrigation_page)
app.register_blueprint(disease_page)
app.register_blueprint(agriguard_page)
app.register_blueprint(weather_page)

# HOME PAGE
@app.route('/')
def home():

    return render_template('dashboard.html')


# RUN APP
if __name__ == '__main__':

    app.run(debug=True)