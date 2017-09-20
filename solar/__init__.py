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
    app = Flask(__name__)
    # app.json_encoder = JSONEncoder
    app.url_map.strict_slashes = False

    @app.after_request
    def set_max_age(response):
        if 'Cache-Control' not in response.headers:
            response.headers['Cache-Control'] = 'max-age={}'.format(0)
        return response
