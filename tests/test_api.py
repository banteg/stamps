import os

import pytest

from stamps.api import api, stats


@pytest.mark.parametrize('query', [
    {'country': 'Switzerland'},
    {'theme': 'Famous people'},
    {'country': 'Canada', 'theme': 'Architecture'},
    {'year': 2007, 'limit': 1},
    {'year': 2002, 'skip': 6},
    {},
])
def test_search(query):
    t = api.search(query)

    assert 'data' in t
    assert t['count'] < 70000
    assert t['count'] > 0


@pytest.mark.skipif('TRAVIS' in os.environ,
                    reason='Travis: text search not enabled')
@pytest.mark.parametrize('query', [
    {'subject': '"pet fish"'},
    {'subject': 'flower -beautiful'},
])
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
@pytest.mark.parametrize('extended', [True, False])
def test_stamp(wns, result, extended):
    t = api.stamp(wns, extended=extended)
    if result:
        assert 'subject' in t
        if extended:
            assert 'set' in t


def test_themes():
    t = api.themes()
    assert 'themes' in t


def test_countries():
    t = api.countries()
    assert 'countries' in t


@pytest.mark.parametrize('f', [
    stats.countries, stats.themes, stats.years
])
def test_api_stats(f):
    t = f()
    assert len(t) > 0
