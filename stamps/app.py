import os

from flask import Flask
from flask.ext.mako import MakoTemplates

from stamps.api.views import api_bp
from stamps.frontend import frontend


def create_app(config):
    app = Flask(__name__)
    MakoTemplates(app)
    config_filename = os.path.join('config', '{}.py'.format(config))
    app.config.from_pyfile(config_filename)

    app.register_blueprint(api_bp, url_prefix='/api')
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
