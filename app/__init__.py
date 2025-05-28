from flask import Flask
import os 
from config import Config
from app.extensions import db, login_manager, migrate
from app.models import User, Product

login_manager.login_view = 'auth.login' #  this sets the login redirect

def create_app():
    app = Flask(__name__)

    # Load correct config based on FLASK_ENV
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.DevelopmentConfig') # settings load here

    db.init_app(app) # setup database
    login_manager.init_app(app) #  setup login manager
    migrate.init_app(app, db)

    # Blueprint registration
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.products import products_bp
    from app.routes.cart import cart_bp
    from app.routes.orders import orders_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(admin_bp)

    @app.context_processor
    def inject_now():
        from datetime import datetime
        return {'current_year': datetime.now().year}
    

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

