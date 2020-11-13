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
            #print(hit)
            if 'schema_name' in hit['_source']:
                label = hit['_source']['schema_name']
                id = hit['_id']
                id_labels.setdefault(id, set()).add(label)
            else:
                continue
    return id_labels

def search(query):
    e = Elasticsearch()
    p = { "query" : { "query_string" : { "query" : query }}}
    response = e.search(index="wikidata_en", body=json.dumps(p))
    id_labels = {}
    if response:
        for hit in response['hits']['hits']:
            #print(hit)
            label = hit['_source']['schema_name']
            id = hit['_id']
            id_labels.setdefault(id, set()).add(label)
    return id_labels

if __name__ == '__main__':
    import sys
    try:
        _, QUERY = sys.argv
    except Exception as e:
        #QUERY = 'Vrije Universiteit Amsterdam'
        QUERY = "Europe"
    for entity, labels in ELSsearch(QUERY).items():
        print(entity, labels)
