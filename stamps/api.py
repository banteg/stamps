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


@api.route('/stamp/<wns>')
def stamp(wns):
    if not wns_re.match(wns):
        abort(404)

    country, serial, year = wns_re.search(wns).groups()

    try:
        data = next(db.stamps.find({'_id': wns}))
    except StopIteration:
        abort(404)

    return jsonify(data)


@api.route('/themes')
def themes():
    themes = db.stamps.distinct('primary_theme')
    primary_themes = [t for t in themes if not '(' in t]
    data = {
        'primary_themes': primary_themes,
        'themes': themes,
    }
    return jsonify(data)


@api.route('/search', methods=['POST'])
def search():
    query = request.get_json()
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
    return jsonify(data)
