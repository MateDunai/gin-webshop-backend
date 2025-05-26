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

--------------------------------------------------
Day 2 — Login system and authentication groundwork
--------------------------------------------------

**Created an auth blueprint to handle user authentication routes (/login, /logout).

**Implemented login functionality accepting POST requests, validating users by username and password.

**Added Flask-Login integration with login_user(), logout_user(), and login_required decorators for session management and protected routes.

**Added password verification using werkzeug.security.check_password_hash.

**Integrated flash messaging system to provide user feedback on login success or failure.

**Setup user loader function (@login_manager.user_loader) to load users by ID for Flask-Login sessions.

**Configured login_manager.login_view to redirect unauthorized users to the login page.

**Added frontend flash message display logic in Jinja templates to show success, error, and info messages with dynamic styling.

**Cleaned up and removed old/deprecated templates in preparation for future frontend work.

**Added products blueprint skeleton with basic GET route to start product-related API endpoints.