from flask.ext.login import UserMixin

from stamps.app import oauth
from stamps.app import get_db

db = get_db()

vk = oauth.remote_app(
    'vk',
    app_key='VK',
    base_url='https://api.vk.com/',
    request_token_url=None,
    access_token_url='https://oauth.vk.com/access_token',
    authorize_url='https://oauth.vk.com/authorize',
)


class VkUser(UserMixin):
    data = {}

    def get_id(self):
        return self.data['_id']

    @staticmethod
    def load(user_id):
        user = db.users.find_one(user_id)
        if user is None:
            return None
        return VkUser(user)

    def save(self):
        db.users.save(self.data)

    def __init__(self, user):
        self.data.update(user)
        self.data.update(_id='vk_{}'.format(user['user_id']))
