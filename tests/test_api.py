import os

import pytest

from stamps.api import api, stats


@pytest.mark.parametrize('query', [
    {'country': 'Switzerland'},
    {'theme': 'Famous people'},
    {'country': 'Canada', 'theme': 'Architecture'},
    {'year': 2007, 'limit': 1},
    {'year': 2002, 'skip': 6},
    {'subject': '"pet fish"'},
    {'subject': 'flower -beautiful'},
])
def test_search(query):
    t = api.search(query)

    assert 'data' in t
    assert t['count'] < 70000
    assert t['count'] > 0


@pytest.mark.parametrize('query', [
    {'subject': '"pet fish"'},
    {'subject': 'flower -beautiful'},
])
@pytest.mark.skipif('TRAVIS' in os.environ,
                    reason='Travis: text search not enabled')
def test_text_search(query):
    t = api.search(query)

    assert 'data' in t
    assert t['count'] < 70000
    assert t['count'] > 0


@pytest.mark.parametrize('wns,result', [
    ('PE080.04', True),
    ('XX000.00', None),
    ('R2D2', None),
])
def test_stamp(wns, result):
    t = api.stamp(wns)
    if not result:
        assert t == result
    else:
        assert 'subject' in t


def test_themes():
    t = api.themes()
    assert 'themes' in t


def test_countries():
    t = api.countries()
    assert 'countries' in t


@pytest.mark.parametrize('f', [
    stats.country, stats.theme, stats.year
])
def test_api_stats(f):
    t = f()
    assert len(t) > 0
