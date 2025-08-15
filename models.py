from app import db

class City(db.Model):
    __tablename__ = 'city'
#atributos columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
