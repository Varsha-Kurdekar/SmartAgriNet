from flask import Blueprint, render_template

# CREATE BLUEPRINT
weather_page = Blueprint(
    'weather_page',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# WEATHER PAGE ROUTE
@weather_page.route('/weather')
def weather():

    return render_template('weather.html')