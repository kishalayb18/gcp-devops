#render_template is for html
#request is for checking whether it is a GET method or POST method
from flask import Flask, render_template, request, jsonify

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
        city = request.form['town']
        api_key = var.key
        weather_data = get_weather(api_key, city)

        ##to print on terminal or postman
        # if weather_data[1]==200:
        #     weather_data=weather_data[0]
        #     req_data={
        #         'city name':weather_data['name'],
        #         'country':weather_data['sys']['country'],
        #         'description':str(weather_data['main']['temp'])+'°C',
        #         'Humidity':str(weather_data['main']['humidity'])+' %',
        #         'Wind Speed':str(weather_data['wind']['speed'])+' m/s'
        #     }
        #     print(req_data)
        # else:
        #     print(weather_data[0])
        
        return render_template('index.html',weather_data=weather_data)
    else:
        return render_template('index.html',weather_data=None)
        # return "will get the datas from postman"

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",8080)), host='0.0.0.0', debug=True)