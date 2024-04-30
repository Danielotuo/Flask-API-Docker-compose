from flask import Flask
from os import environ
from .models import db
from .routes import routes_bp


def create_app():
    """
    Application factory function that creates and configures the Flask app.
    """
    app = Flask(__name__)

    # Read the database password from the secret file
    db_password = open('/run/secrets/db_password', 'r').read().strip()
    db_user = environ.get('DB_USER')
    db_name = environ.get('DB_NAME')
    db_url = f"postgresql://{db_user}:{db_password}@flask_db:5432/{db_name}"

    # Configure the database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Register the routes blueprint
    app.register_blueprint(routes_bp)

    return app
