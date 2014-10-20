from flask import Blueprint
from pymongo import MongoClient


frontend = Blueprint('frontend', __name__)

mongo = MongoClient()
db = mongo.stamps


@frontend.route('/')
def index():
    return 'Hello'
