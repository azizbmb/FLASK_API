#API-KEY = c6d7b00d2e184315b1c4342125190

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Remplacez par votre clé API OpenWeatherMap
API_KEY = 'c6d7b00d2e184315b1c4342125190'
BASE_URL = 'http://api.weatherapi.com/v1/forecast.json'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = {}
    if request.method == 'POST':
        city = request.form['city']
        params = {
            'key': API_KEY,
            'q': city,
            'aqi': 'no'  # Ne pas inclure la qualité de l'air
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {'error': 'Ville non trouvée ou erreur API'}
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)