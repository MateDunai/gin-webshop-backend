from app import create_app, db


app = create_app()

if app.config.get('ENV') == 'development':
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app.run(debug=app.config.get('DEBUG', True))