from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
api = Api()


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    db.init_app(app)
    api = Api(app)

    from oxford.endpoints import HelloWorld
    api.add_resource(HelloWorld, '/')

    return app
