from flask import Flask
import os
from src.auth import auth
from src.api import api
from src.database import db
from flask_jwt_extended import JWTManager

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(test_config=None):
    app = Flask(__name__,
                instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'database.db.db'),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY') or 'dummy_secret_key'
        )
    else:
        app.config.from_mapping(test_config)

    db.app = app
    db.init_app(app)
    JWTManager(app)
    app.register_blueprint(auth)
    app.register_blueprint(api)

    return app
