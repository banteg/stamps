from flask import Flask
from flask.ext.mako import MakoTemplates
from flask.ext.pymongo import PyMongo
from flask_oauthlib.client import OAuth


mako = MakoTemplates()
mongo = PyMongo()
oauth = OAuth()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object('stamps.config.{}'.format(config))

    mako.init_app(app)

    mongo.init_app(app)
    mongo.app = app

    oauth.init_app(app)

    from stamps.auth.views import auth
    app.register_blueprint(auth, url_prefix='/auth')

    from stamps.api.views import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from stamps.frontend import frontend
    app.register_blueprint(frontend)

    return app


def develop():
    app = create_app('debug')
    app.run('127.0.0.1', 8000)


def get_db():
    with mongo.app.app_context():
        return mongo.db


if __name__ == '__main__':
    develop()
