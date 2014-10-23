def test_empty_db(db):
    t = db.stamps.count()
    assert t > 0


def test_schema(db):
    t = next(db.stamps.find())
    need = [
        'subject',
        'country',
        'date',
        'issuer',
        'printer',
        'size',
        'theme',
        'denomination',
        'image',
        'set',
        'perforations',
        'layout',
    ]

    for field in need:
        assert field in t
