from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from .service import extract_weather_data
import requests
import os

app = Flask(__name__)
CORS(app)
key = os.getenv('KEY')

load_dotenv()

@app.route('/get-weather')
def get_weather():
    location = request.args.get('location')
    print(location)
    if location:
        url_city_data = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={os.getenv("KEY")}'
        response = requests.get(url_city_data)
        data = response.json()
        return jsonify(data)
    else:
        return jsonify(error='Location not provided'), 400

@app.route('/get-weather-forecast')
def get_weather_forecast():
   location = request.args.get('location')
   if location:
       url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={os.getenv("KEY")}&units=metric'
       response = requests.get(url)
       data = response.json()
       forecast = []
       print(data)
       for entry in data['list']:
           extracted_data = extract_weather_data(entry)
           forecast.append(extracted_data)
       return jsonify(forecast)
   else:
       return jsonify(error='Location not provided'), 400

if __name__ == '__main__':
    app.run(debug=True)
