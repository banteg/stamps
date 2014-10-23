import os

from flask import Flask
from flask.ext.mako import MakoTemplates

from stamps.db import mongo


def create_app(config):
    app = Flask(__name__)
    MakoTemplates(app)
    config_filename = os.path.join('config', '{}.py'.format(config))
    app.config.from_pyfile(config_filename)

    mongo.init_app(app)
    mongo.app = app

    from stamps.api.views import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from stamps.frontend import frontend
    app.register_blueprint(frontend)

    return app


def develop():
    app = create_app('debug')
    app.run('127.0.0.1', 8000)


def wsgi():
    app = create_app('production')
    return app

if __name__ == '__main__':
    develop()
