from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import db, User

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login' #  this sets the login redirect

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # settings load here

    db.init_app(app) # setup database
    login_manager.init_app(app) #  setup login manager

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.products import products_bp
    app.register_blueprint(products_bp)


    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
