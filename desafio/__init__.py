from flask import Flask
import os
from desafio.auth.auth import auth
from desafio.api.api import api
from desafio.util.errors import errors
from desafio.database import db
from flask_jwt_extended import JWTManager
from desafio.util.custom_logger import LogHandler
from flask.logging import default_handler
from logging import DEBUG

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(test_config=False):
    app = Flask(__name__,
                instance_relative_config=True)

    if test_config:
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    db.app = app
    db.init_app(app)
    JWTManager(app)
    app.register_blueprint(auth)
    app.register_blueprint(api)
    app.register_blueprint(errors)
    app.logger.removeHandler(default_handler)
    app.logger.addHandler(LogHandler())
    app.logger.setLevel(DEBUG)

    return app
