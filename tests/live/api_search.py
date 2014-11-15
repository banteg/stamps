from time import clock
from random import randint, choice, sample
from statistics import mean, median

from pymongo import MongoClient
import requests

db = MongoClient().stamps

ENDPOINT = 'http://localhost:8000/api/search'
N = 100

years = list(range(2002, 2015))
themes = list(db.stats.find_one('themes')['themes'])
countries = list(db.stats.find_one('countries')['countries'])

QUERY = {
    'year': years,
    'theme': themes,
    'country': countries,
}


def random_query():
    n = randint(0, 3)
    q = sample(list(QUERY), n)
    query = {x: choice(QUERY[x]) for x in q}
    query.update(limit=10)

    return query


def search(query):
    return requests.post(ENDPOINT, json=query).json()

times = []
start = clock()

for i in range(N):
    istart = clock()
    query = random_query()
    result = search(query)
    itime = clock()-istart
    times.append(itime)
    print('{:03d}: {:5.3f}s, {} found with {}'.format(i, itime, result['count'], query))

ttime = clock()-start
print('finished in {:5.3f}s, mean {:5.3f}s, median {:5.3f}s'.format(ttime, mean(times), median(times)))
