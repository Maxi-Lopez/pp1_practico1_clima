from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Diccionario de ciudades y coordenadas
ciudades = {
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816},
    "Córdoba": {"lat": -31.4201, "lon": -64.1888},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Nueva York": {"lat": 40.7128, "lon": -74.0060},
    "Tokio": {"lat": 35.6895, "lon": 139.6917},
    "París": {"lat": 48.8566, "lon": 2.3522},
    "Londres": {"lat": 51.5074, "lon": -0.1278},
    "Sídney": {"lat": -33.8688, "lon": 151.2093},
    "Ciudad de México": {"lat": 19.4326, "lon": -99.1332},
    "El Cairo": {"lat": 30.0444, "lon": 31.2357}
}

@app.route('/')
def index():
    return render_template('index.html', ciudades=ciudades.keys())

@app.route('/clima')
def clima():
    nombre_ciudad = request.args.get("ciudad")
    datos_ciudad = ciudades.get(nombre_ciudad)

    lat = datos_ciudad["lat"]
    lon = datos_ciudad["lon"]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)

    data = response.json()
    clima_actual = data.get("current_weather", {})

    return render_template("clima.html", ciudad=nombre_ciudad, clima=clima_actual)

