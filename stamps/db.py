from flask.ext.pymongo import PyMongo

mongo = PyMongo()


def db():
    with mongo.app.app_context():
        return mongo.db
