from flask import Blueprint, abort
from flask.ext.mako import render_template

from stamps.api import api, stats

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    countries = stats.countries()
    themes = stats.themes()

    return render_template('index.slim',
                           countries=countries,
                           themes=themes)


@frontend.route('/explore')
def search():
    return render_template('search.slim')


@frontend.route('/stamp/<wns>')
def stamp(wns):
    stamp = api.stamp(wns)
    if not stamp:
        abort(404)

    return render_template('stamp.slim', stamp=stamp)


@frontend.route('/templates/ministamp.slim')
def ministamp():
    return render_template('ministamp.slim')
