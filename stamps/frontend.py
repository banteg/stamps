from flask import Blueprint, render_template
from pymongo import MongoClient


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
