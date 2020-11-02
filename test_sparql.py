import trident
import json

KBPATH='assets/wikidata-20200203-truthy-uri-tridentdb'

#Retrieve first 10 entities of type (P31) city (Q515)
query="PREFIX wde: <http://www.wikidata.org/entity/> "\
    "PREFIX wdp: <http://www.wikidata.org/prop/direct/> "\
    "PREFIX wdpn: <http://www.wikidata.org/prop/direct-normalized/> "\
    "select ?s where { ?s wdp:P31 wde:Q515 . } LIMIT 10"

# Load the KB
db = trident.Db(KBPATH)
results = db.sparql(query)
json_results = json.loads(results)

print("*** VARIABLES ***")
variables = json_results["head"]["vars"]
print(variables)

print("\n*** BINDINGS ***")
results = json_results["results"]
for b in results["bindings"]:
    line = ""
    for var in variables:
        line += var + ": " + b[var]["value"] + " "
    print(line)

print("\n*** STATISTICS ***")
print(json_results['stats'])
