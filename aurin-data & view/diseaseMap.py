import json
import re
import couch

#create a map for attributes
with open('diseasemeta.json') as f:
    diseasemeta = f.read()

obj = json.loads(diseasemeta)
list = obj['selectedAttributes']  # unwrapping

attribute_map = {}

for item in list:
    key = item['name']
    title = item['title']
    attribute_map[key] = title

print (attribute_map)


# couch.upload("aurin_disease", attribute_map)
