from flask import url_for
from json import loads, dumps
import pytest


def json(c):
    return loads(c.data.decode('utf-8'))


def test_api_stamp_url(context):
    wns = 'PE080.04'
    with context:
        stamp = url_for('api.stamp', wns=wns)
    assert stamp == '/api/stamp/{}'.format(wns)


@pytest.mark.parametrize('url', [
    'themes', 'countries'
])
def test_api_urls(context, url):
    with context:
        t = url_for('api.{}'.format(url))

    assert t == '/api/{}'.format(url)


@pytest.mark.parametrize('a,b', [
    ('theme', 'themes'),
    ('country', 'countries'),
    ('year', 'years')
])
def test_stats_urls(context, a, b):
    with context:
        t = url_for('api.stats_{}'.format(a))

    assert t == '/api/stats/{}'.format(b)


@pytest.mark.parametrize('wns,status_code', [
    ('PE080.04', 200),
    ('R2D2', 404),
    ('whatever', 404)
])
def test_api_stamp(client, wns, status_code):
    c = client.get('/api/stamp/{}'.format(wns))

    assert c.status_code == status_code

    if c.status_code == 200:
        assert c.headers['content-type'] == 'application/json'
        assert 'subject' in json(c)


@pytest.mark.parametrize('endpoint,sample', [
    ('countries', 'Canada'),
    ('themes', 'Flora')
])
def test_api_countries(client, endpoint, sample):
    c = client.get('/api/{}'.format(endpoint))
    j = json(c)

    assert c.status_code == 200
    assert c.headers['content-type'] == 'application/json'
    assert endpoint in j
    assert len(j[endpoint]) > 0
    assert sample in j[endpoint]


@pytest.mark.parametrize('endpoint', [
    'countries', 'themes', 'years'
])
def test_api_stats_countries(client, endpoint):
    c = client.get('/api/stats/{}'.format(endpoint))
    j = json(c)

    assert c.status_code == 200
    assert c.headers['content-type'] == 'application/json'
    assert 'data' in j
    assert len(j['data']) > 0


def test_api_search_get_fail(client):
    c = client.get('/api/search')
    assert c.status_code == 405


@pytest.mark.parametrize('query', [
    {},
    {'country': 'Canada'},
    {'theme': 'Flora'},
    {'country': 'Switzerland', 'theme': 'Fauna'},
    {'year': 2007, 'limit': 1},
    {'year': 2002, 'country': 'Zimbabwe'},
])
def test_api_search_1(client, query):
    print(query)
    c = client.post('/api/search',
                    data=dumps(query),
                    content_type='application/json')
    j = json(c)

    assert c.status_code == 200
    assert c.headers['content-type'] == 'application/json'
    assert 'data' in j
