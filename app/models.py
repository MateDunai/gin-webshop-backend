from app.extensions import db
from flask_login import UserMixin

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key
    name = db.Column(db.String(100), nullable=False) 
    price = db.Column(db.Float, nullable=False) 
    description = db.Column(db.Text, nullable=True) # optional
    image_url = db.Column(db.Text, nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False) # password, hash later
    is_admin = db.Column(db.Boolean, default=False)