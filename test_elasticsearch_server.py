import requests
import json
import time
from elasticsearch import Elasticsearch


def ELSsearch(query):
    e = Elasticsearch()
    p = { "query" : { "query_string" : { "query" : query }} }
    try:
        response = e.search(index="wikidata_en", body=json.dumps(p))
    except:
        return {}

    id_labels = {}
    if response:
        for hit in response['hits']['hits']:
            label = hit['_source']['schema_name']
            id = hit['_id']
            id_labels.setdefault(id, set()).add(label)
    return id_labels

def search(query):
    e = Elasticsearch()
    p = { "query" : { "query_string" : { "query" : query }}}
    response = e.search(index="wikidata_en", body=json.dumps(p))
    id_labels = {}
    if response:
        for hit in response['hits']['hits']:
            label = hit['_source']['schema_name']
            id = hit['_id']
            id_labels.setdefault(id, set()).add(label)
    return id_labels
'''
def find_ten_candidates(query,Num=10):
    retry_time = 2
    while retry_time > 0:
        retry_time -=1
        try:
            e = Elasticsearch()
            p = { "query" : { "query_string" : { "query" : query }},"size" : 20 }
            response = e.search(index="wikidata_en", body=json.dumps(p))
            break
        except:
            time.sleep(2)

    best_ten_id_labels = {}
    # id_labels : []
    id_labels = []
'''
if __name__ == '__main__':
    import sys
    try:
        _, QUERY = sys.argv
    except Exception as e:
        QUERY = 'Vrije Universiteit Amsterdam'

    for entity, labels in search(QUERY).items():
        print(entity, labels)
