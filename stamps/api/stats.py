from stamps.app import get_db

db = get_db()


def theme():
    q = db.stamps.aggregate([
        {'$unwind': '$theme'},
        {'$group': {
            '_id': '$theme',
            'count': {'$sum': 1}
        }},
        {'$sort': {'count': -1}},
    ])
    return q['result']


def country():
    q = db.stamps.aggregate([
        {'$group': {
            '_id': '$country',
            'count': {'$sum': 1}
        }},
        {'$sort': {'count': -1}},
    ])
    return q['result']


def year():
    q = db.stamps.aggregate([
        {'$group': {
            '_id': {'$year': '$date'},
            'count': {'$sum': 1}
        }},
        {'$sort': {'count': -1}},
    ])
    return q['result']
