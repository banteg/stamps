from flask import Blueprint, render_template, abort
from pymongo import MongoClient

from stamps import api


frontend = Blueprint('frontend', __name__)

mongo = MongoClient()
db = mongo.stamps


@frontend.route('/')
def index():
    countries = db.stamps.distinct('country')
    themes = db.stamps.distinct('primary_theme')
    primary_themes = [t for t in themes if t and not '(' in t]

    return render_template('index.html',
                           countries=countries,
                           themes=primary_themes)


@frontend.route('/search')
def search():
    return render_template('search.html')


@frontend.route('/stamp/<wns>')
def stamp(wns):
    stamp = api.stamp(wns)
    if not stamp:
        abort(404)

    return render_template('stamp.html', stamp=stamp)
