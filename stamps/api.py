import re

from flask import Blueprint, abort, jsonify
from pymongo import MongoClient


api = Blueprint('api', __name__)
wns_re = re.compile('([A-Z]{2})(\d{3})\.(\d{2})')

mongo = MongoClient()
db = mongo.stamps


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
