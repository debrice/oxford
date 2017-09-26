# -*- coding: utf-8 -*-
"""
    oxford
    ~~~~~~
    this module contains the Oxford Rest API logic powered by Flask.
"""
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

    # loads the root search endpoint "/?word=wolf"
    from oxford.endpoints import OxfordDictionaryAPI
    api.add_resource(OxfordDictionaryAPI, '/')

    return app
