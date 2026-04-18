import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
    )

    # Load config
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Import and register routes (IMPORTANT)
    from app.routes import main
    app.register_blueprint(main)

    return app