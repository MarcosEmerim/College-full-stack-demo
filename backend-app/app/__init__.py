import os
from flask import Flask
from flask_cors import CORS

from app.extensions import db, migrate, api

from app.controller.unidade_controller import api as unidade_ns
from app.controller.cadeiras_controller import api as cadeiras_ns

class DevelopmentConfig():
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    api.add_namespace(cadeiras_ns, path="/cadeiras")
    api.add_namespace(unidade_ns, path="/unidade")

    return app