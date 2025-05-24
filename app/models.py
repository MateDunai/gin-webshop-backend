from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key
    title = db.Column(db.String(100), nullable=False) 
    price = db.Column(db.Float, nullable=False) 
    description = db.Column(db.Text, nullable=True) # optional

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False) 
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(60), nullable=False) # password, hash later