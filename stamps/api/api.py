import re
from datetime import datetime

from stamps.app import get_db

db = get_db()


def stamp(wns, extended=True):
    if not re.match('[A-Z]{2}\d{3}\.\d{2}', wns):
        return None

    data = db.stamps.find_one(wns)
    if data is None:
        return None

    if extended and 'set' in data:
        other = db.stamps.find(
            {'_id': {'$in': data['set']}},
            {'image': 1}
        )
        data['set'] = list(other)

    return data


def themes():
    themes = db.stats.find_one('themes')['themes']
    return {'themes': list(themes)}


def countries():
    countries = db.stats.find_one('countries')['countries']
    return {'countries': list(countries)}


def year_filter(query):
    year = query.pop('year')
    query['date'] = {
        '$gte': datetime(year, 1, 1),
        '$lt': datetime(year + 1, 1, 1)
    }
    return query


def subject_filter(query):
    subject = query.pop('subject')
    query['$text'] = {
        '$search': subject,
    }
    return query


def search(query):
    skip = int(query.get('skip', 0))
    limit = int(query.get('limit', 10))
    limit = min(limit, 100)
    query.pop('skip', None)
    query.pop('limit', None)
    query = {k: v for k, v in query.items() if v}
    if 'year' in query:
        query = year_filter(query)
    if 'subject' in query:
        query = subject_filter(query)

    results = db.stamps.find(query).skip(skip).limit(limit)
    count = results.count()

    data = {
        'count': count,
        'skip': skip,
        'limit': limit,
        'data': list(results),
        'query': query,
    }

    return data
