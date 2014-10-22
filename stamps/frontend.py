from flask import Blueprint, abort
from flask.ext.mako import render_template
from pymongo import MongoClient

from stamps.api import api, stats


frontend = Blueprint('frontend', __name__)

mongo = MongoClient()
db = mongo.stamps


@frontend.route('/')
def index():
    countries = stats.country()
    themes = stats.theme()
    themes = [t for t in themes if t['_id']]

    return render_template('index.html',
                           countries=countries,
                           themes=themes)


@frontend.route('/explore')
def search():
    return render_template('search.html')


@frontend.route('/stamp/<wns>')
def stamp(wns):
    stamp = api.stamp(wns)
    if not stamp:
        abort(404)

    return render_template('stamp.html', stamp=stamp)
