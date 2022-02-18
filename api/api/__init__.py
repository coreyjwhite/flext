"""Flask app factory module."""

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Make SQLAlchemy object available globally for ORM models
db = SQLAlchemy()


def create_app(config=Config):
    """Flask app factory."""

    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize plugins
    db.init_app(app)
    api = Api(app)
    CORS(app)

    # Add REST endpoints and OpenAPI specs
    with app.app_context():
        from .specs import add_specs
        from .resources import add_resources

        add_resources(api)
        add_specs()
        db.create_all()

    return app
