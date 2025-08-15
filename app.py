from flask import Flask, render_template, request
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_clima'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import City

ciudades = {
    "Buenos Aires CABA": {"lat": -34.6037, "lon": -58.3816},
    "Cordoba": {"lat": -31.4201, "lon": -64.1888},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Nueva York": {"lat": 40.7128, "lon": -74.0060},
    "Tokio": {"lat": 35.6895, "lon": 139.6917},
    "Paris": {"lat": 48.8566, "lon": 2.3522},
    "Londres": {"lat": 51.5074, "lon": -0.1278},
    
    "Ciudad de Mexico": {"lat": 19.4326, "lon": -99.1332},
    "El Cairo": {"lat": 30.0444, "lon": 31.2357},
}

@app.route("/")
def index():
    return render_template("index.html", ciudades=ciudades)

@app.route("/clima")
def clima():
    ciudad = request.args.get("ciudad")

    if ciudad not in ciudades:
        return "Ciudad no encontrada", 404

    lat = ciudades[ciudad]["lat"]
    lon = ciudades[ciudad]["lon"]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    respuesta = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if respuesta.status_code != 200:
        return "Error al obtener el clima", 500

    datos_clima = respuesta.json().get("current_weather", {})
    return render_template("clima.html", ciudad=ciudad, clima=datos_clima)

if __name__ == "__main__":
    app.run(debug=True)
