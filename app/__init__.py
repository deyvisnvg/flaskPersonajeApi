from flask import Flask
from .config import Config
from flask_bootstrap import Bootstrap

from app.routes.personaje import bp_personaje


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.register_blueprint(bp_personaje)

    Bootstrap(app)

    return app
