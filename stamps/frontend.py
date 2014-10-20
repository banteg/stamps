from flask import Blueprint, render_template
from pymongo import MongoClient


frontend = Blueprint('frontend', __name__)

mongo = MongoClient()
db = mongo.stamps


@frontend.route('/')
def index():
    countries = db.stamps.distinct('country')
    return render_template('index.html', countries=countries)
