from flask import Blueprint, abort, request, jsonify

from stamps.api import api, stats

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/stamp/<wns>')
def stamp(wns):
    data = api.stamp(wns)

    if not data:
        abort(404)
    return jsonify(data)


@api_bp.route('/themes')
def themes():
    data = api.themes()
    return jsonify(data)


@api_bp.route('/countries')
def countries():
    data = api.countries()
    return jsonify(data)


@api_bp.route('/search', methods=['POST'])
def search():
    query = request.get_json()
    if not query:
        query = {}

    data = api.search(query)
    return jsonify(data)


@api_bp.route('/stats/themes')
def stats_theme():
    data = stats.themes()
    return jsonify(data=data)


@api_bp.route('/stats/countries')
def stats_country():
    data = stats.countries()
    return jsonify(data=data)


@api_bp.route('/stats/years')
def stats_year():
    data = stats.years()
    return jsonify(data=data)
