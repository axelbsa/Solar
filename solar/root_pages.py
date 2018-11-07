import logging
logger = logging.getLogger(__name__)

from flask import request, jsonify
from voluptuous import Optional, Required, Schema

from solar.calculations import sun_rise, sun_set


def init_pages(app):
    from db import db

    db.app = app
    db.init_app(app)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            return jsonify(Post=True)
        else:
            return jsonify(GET=True)

    @app.route('/main', methods=['GET'])
    def render_main():
        print request.args
        return "123"

    @app.route('/sun-rise', methods=['POST', 'GET'])
    def calculate_sun_rise():
        sun_rise_params = Schema({
            Required("city", default="oslo"): basestring,
            Optional("date", default=""): basestring
        })

        logger.debug("params:{}".format(dict(request.args)))
        params = ""
        if request.method == "POST":
            params = sun_rise_params(request.json)
        elif request.method == "GET":
            _t = {k: "".join(v) for k, v in request.args.iteritems()}
            logger.debug("_t = {}".format(_t))
            params = sun_rise_params(_t)

        next_rise = sun_rise(params["city"])

        if not next_rise:
            return jsonify({"results": False})

        next_rise = next_rise.isoformat()
        return jsonify(next_sun_rise_from_position=next_rise)

    @app.route('/sun-set', methods=['POST', 'GET'])
    def calculate_sun_set():
        sun_rise_params = Schema({
            Required("city", default="oslo"): basestring,
            Optional("date", default=""): basestring
        })

        params = ""
        if request.method == "POST":
            params = sun_rise_params(request.json)
        elif request.method == "GET":
            _t = {k: "".join(v) for k, v in request.args.iteritems()}
            logger.debug("_t = {}".format(_t))
            params = sun_rise_params(_t)

        next_set = sun_set(params["city"])
        if not next_set:
            return jsonify({"results": False})

        next_set = next_set.isoformat()
        return jsonify(next_sun_set_from_position=next_set)

    @app.route('/programming', methods=['GET', 'POST'])
    def render_programming():
        return 123
