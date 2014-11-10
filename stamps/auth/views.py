from flask import Blueprint, url_for
from flask_oauthlib.client import OAuthException
from flask.ext.login import login_user, logout_user, current_user, login_required

from stamps.auth.vk import vk, VkUser
from stamps.app import login, get_db

auth = Blueprint('auth', __name__)
db = get_db()


@login.user_loader
def load_user(user_id):
    return VkUser.load(user_id)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return 'ok'


@auth.route('/vk')
def vk_oauth():
    callback = url_for('auth.vk_callback', _external=True)
    return vk.authorize(callback=callback)


@auth.route('/vk/callback')
def vk_callback():
    resp = vk.authorized_response()
    if isinstance(resp, OAuthException):
        return resp.message

    user = VkUser(resp)
    user.save()
    login_user(user)

    return current_user.get_id()
