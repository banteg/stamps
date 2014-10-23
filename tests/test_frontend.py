import pytest
from flask import url_for


def test_urls(context):
    with context:
        assert url_for('frontend.index') == '/'
        assert url_for('frontend.search') == '/explore'


def test_stamp_url(client, context):
    with context:
        t = url_for('frontend.stamp', wns='PE080.04')
    assert t == '/stamp/PE080.04'


def test_index(client):
    c = client.get('/')
    assert c.status_code == 200


def test_explore(client, context):
    c = client.get('/explore')
    assert c.status_code == 200


@pytest.mark.parametrize('wns,status_code', [
    ('PE080.04', 200),
    ('XX000.00', 404),
    ('R2D2', 404),
])
def test_stamp(client, wns, status_code):
    c = client.get('/stamp/{}'.format(wns))
    assert c.status_code == status_code
