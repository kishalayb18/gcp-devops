#render_template is for html
#request is for checking whether it is a GET method or POST method
from flask import Flask, render_template, request

#requests is for weather data
import requests

import var
import os

from getWeather import get_weather

#creating the flask object
app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        api_key = var.key
        weather_data = get_weather(api_key, city)
        return render_template('index.html',weather_data=weather_data)
    else:
        return render_template('index.html',weather_data=None)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",8080)), host='0.0.0.0', debug=True)
