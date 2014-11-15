from operator import itemgetter

from stamps.app import get_db

db = get_db()


def themes():
    q = db.stats.find_one({'_id': 'themes'})
    s = sorted(q['themes'].items(), key=itemgetter(1), reverse=True)
    return s


def countries():
    q = db.stats.find_one({'_id': 'countries'})
    s = sorted(q['countries'].items(), key=itemgetter(1), reverse=True)
    return s


def years():
    q = db.stats.find_one({'_id': 'years'})
    s = sorted(q['years'].items(), key=itemgetter(1), reverse=True)
    return s
