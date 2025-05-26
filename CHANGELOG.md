Progress Log — Flask Gin Webshop Backend
-----------------------------
Day 1 — Foundations laid down
-----------------------------
**Created a Flask app using the app factory pattern (create_app() in __init__.py).

**Separated configuration into a config.py file for cleaner management of secrets and environment variables.

**Integrated SQLAlchemy ORM, instantiated db = SQLAlchemy(), and linked it with the Flask app (db.init_app(app)).

**Designed database models (User, Product) in models.py as Python classes representing tables.

**Imported the models inside __init__.py so SQLAlchemy knows about them.

**Created a run.py file to initialize the app context and run db.create_all() to build the actual tables in the database.

**Gained an understanding of why importing models before creating tables is necessary.

**Ready to start implementing CRUD routes (Create, Read, Update, Delete) for product management.

