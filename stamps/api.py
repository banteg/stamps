import re

from flask import Blueprint, Response, abort, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps


api = Blueprint('api', __name__)
wns_re = re.compile('([A-Z]{2})(\d{3})\.(\d{2})')

mongo = MongoClient()
db = mongo.stamps


def bsonify(data):
    return Response(dumps(data, indent=2, ensure_ascii=False),
                    mimetype='application/json')


def stamp(wns):
    if not wns_re.match(wns):
        return None

    try:
        data = next(db.stamps.find({'_id': wns}))
    except StopIteration:
        return None

    return data


def themes():
    themes = db.stamps.distinct('primary_theme')
    primary_themes = [t for t in themes if not '(' in t]
    data = {
        'primary_themes': primary_themes,
        'themes': themes,
    }

    return data


def countries():
    countries = db.stamps.distinct('country')
    data = {
        'countries': countries,
    }

    return data


def search(query):
    skip = int(query.get('skip', 0))
    limit = int(query.get('limit', 10))
    limit = min(limit, 100)
    query.pop('skip', None)
    query.pop('limit', None)

    results = db.stamps.find(query).skip(skip).limit(limit)
    count = results.count()

    data = {
        'count': count,
        'skip': skip,
        'limit': limit,
        'data': list(results),
    }

    return data


@api.route('/stamp/<wns>')
def stamp_route(wns):
    data = stamp(wns)

    if not data:
        abort(404)
    return jsonify(data)


@api.route('/themes')
def themes_route():
    data = themes()
    return jsonify(data)


@api.route('/countries')
def countries_route():
    data = countries()
    return jsonify(data)


@api.route('/search', methods=['POST'])
def search_route():
    query = request.get_json()
    if not query:
        query = {}

    data = search(query)
    return jsonify(data)
