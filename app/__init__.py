from flask import Flask
from config import Config
from app.extensions import db, login_manager
from app.models import User, Product

login_manager.login_view = 'auth.login' #  this sets the login redirect

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # settings load here

    db.init_app(app) # setup database
    login_manager.init_app(app) #  setup login manager

    # Blueprint registration
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.products import products_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
