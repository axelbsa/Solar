# -*- encoding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

from flask import Flask


def create_app():
    args = {}
    app = Flask(__name__, **args)
    # app.config.from_object('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://axelbs:axelbs@10.0.0.20/world"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config.from_pyfile('conf/config.py')
    app.config.update(SECRET_KEY='development key_____!!!skgtg20')

    from root_pages import init_pages
    init_pages(app)

    return app
