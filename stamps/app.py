from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
mongo = MongoClient()
db = mongo.stamps


@app.route('/')
def index():
    ...


def main():
    app.debug = True
    app.run('127.0.0.1', 8000)


if __name__ == '__main__':
    main()
