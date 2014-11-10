from stamps.app import oauth


vk = oauth.remote_app(
    'vk',
    app_key='VK',
    base_url='https://api.vk.com/',
    request_token_url=None,
    access_token_url='https://oauth.vk.com/access_token',
    authorize_url='https://oauth.vk.com/authorize',
)
