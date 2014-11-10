from flask import Blueprint, url_for, jsonify

from stamps.auth.vk import vk

auth = Blueprint('auth', __name__)


@auth.route('/vk')
def vk_oauth():
    callback = url_for('auth.vk_callback', _external=True)
    return vk.authorize(callback=callback)


@auth.route('/vk/callback')
def vk_callback():
    resp = vk.authorized_response()
    if resp is None:
        return 'error'
    return jsonify(resp)
