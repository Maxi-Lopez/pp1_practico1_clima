from flask import Flask, render_template, request
import requests

app = Flask(__name__)

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

descripciones_weathercode = {
    0: "Despejado",
    1: "Principalmente despejado",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Niebla",
    48: "Niebla con escarcha",
    51: "Llovizna ligera",
    53: "Llovizna moderada",
    55: "Llovizna intensa",
    61: "Lluvia ligera",
    63: "Lluvia moderada",
    65: "Lluvia intensa",
    71: "Nieve ligera",
    73: "Nieve moderada",
    75: "Nieve intensa",
    80: "Chubascos ligeros",
    81: "Chubascos moderados",
    82: "Chubascos violentos",
    95: "Tormenta eléctrica",
    96: "Tormenta con granizo leve",
    99: "Tormenta con granizo severo"
}



@app.route('/')
def index():
    return render_template('index.html', ciudades=ciudades.keys())

@app.route('/clima')
def clima():
    nombre_ciudad = request.args.get("ciudad")
    datos_ciudad = ciudades.get(nombre_ciudad)

    latitud = datos_ciudad["lat"]
    longitud = datos_ciudad["lon"]

    direccion = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true"
    response = requests.get(direccion).json()
    clima_actual = response.get("current_weather")
    codigo = clima_actual["weathercode"]
    codigo_clima = descripciones_weathercode.get(codigo)
    
    return render_template("clima.html", ciudad=nombre_ciudad, clima=clima_actual, code=codigo_clima)

