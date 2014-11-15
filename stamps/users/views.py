from flask import Blueprint, abort
from flask.ext.mako import render_template

from stamps.app import get_db

db = get_db()

users = Blueprint('users', __name__, url_prefix='/user')


@users.route('/<slug>')
def user_detail(slug):
    user = db.users.find_one({'slug': slug})

    if user is None:
        return abort(404)

    stamps = db.stamps.find(
        {'_id': {'$in': user['likes']}},
        {'image': 1, 'subject': 1, 'country': 1},
    )

    return render_template(
        'user_detail.slim',
        user=user, stamps=stamps
    )
