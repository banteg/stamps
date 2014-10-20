from flask import Flask

from stamps.api import api
from stamps.frontend import frontend


app = Flask(__name__)
app.config.update(JSON_AS_ASCII=False)

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(frontend)


def main():
    app.debug = True
    app.run('127.0.0.1', 8000)


if __name__ == '__main__':
    main()
