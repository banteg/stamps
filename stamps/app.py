from flask import Flask
from flask.ext.mako import MakoTemplates
from plim import preprocessor

from stamps.api.views import api_bp
from stamps.frontend import frontend


app = Flask(__name__)
mako = MakoTemplates(app)
app.config.update(
    JSON_AS_ASCII=False,
    MAKO_PREPROCESSOR=preprocessor,
    MAKO_TRANSLATE_EXCEPTIONS=False
)

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(frontend)


def main():
    app.debug = True
    app.run('127.0.0.1', 8000)


if __name__ == '__main__':
    main()
