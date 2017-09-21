# -*- encoding: utf-8 -*-
import logging
logger = logging.getLogger(__name__)

import datetime
import psycopg2
from sqlalchemy.exc import SQLAlchemyError

from flask import Flask, session as session_data, jsonify, json, request
from flask_principal import Principal, PermissionDenied
from werkzeug.routing import BaseConverter


def create_app():
    args = {}
    # args['instance_path'] = '/home/axelbsa/src/hound/hound'
    app = Flask(__name__, **args)
    # app.config.from_pyfile('conf/config.py')
    app.config.update(SECRET_KEY='development key_____!!!skgtg20')

    from root_pages import init_pages
    init_pages(app)

    return app
