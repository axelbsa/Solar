from voluptuous import All, Any, Coerce, In, Optional, Required, Schema
from flask import render_template, session, request, jsonify

from solar.calculations import sun_rise, sun_set


def init_pages(app):

    @app.before_first_request
    def startup():
        pass
        # from db import connect
        # pg, meta = connect()

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            return jsonify(Post=True)
        else:
            return jsonify(GET=True)

    @app.route('/main', methods=['GET'])
    def render_main():
        return 123

    @app.route('/sun-rise', methods=['POST'])
    def calculate_sun_rinse():
        sun_rise_params = Schema({
            Required("city_name", default="oslo, norway"): basestring,
            Optional("date", default=""): basestring
        })
        print request.json
        params = sun_rise_params(request.json)
        next_rise = sun_rise(params["city_name"])
        return jsonify(next_sun_rise_from_position=next_rise)

    @app.route('/sun-set', methods=['POST'])
    def calculate_sun_set():
        sun_rise_params = Schema({
            Required("city_name", default=None): basestring,
            Optional("date", default=""): basestring
        })
        print request.json
        params = sun_rise_params(request.json)
        next_rise = sun_set(params["city_name"])
        return jsonify(next_sun_set_from_position=next_rise)

    @app.route('/programming', methods=['GET', 'POST'])
    def render_programming():
        return 123
