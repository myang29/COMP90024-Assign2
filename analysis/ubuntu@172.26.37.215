import couchdb

input_address = "http://115.146.92.83:8022"
out_address = "http://172.26.38.75:9024"

couch_input = couchdb.Server(input_address)
couch_out = couchdb.Server(out_address)

db_input = couch_input['processed_twit']

try:
    db_out = couch_out['processed_twit']
except:
    db_out = couch_out.create('processed_twit')


for id in db_input:
    doc = {
        'id': db_input[id]['id'],
        'created_at':db_input[id]['created_at'],
        'coordinates':db_input[id]['coordinates'],
        'text': db_input[id]['text'],
        'wrath':db_input[id]['wrath'],
        'code':db_input[id]['code']
    }
    db_out.save(doc)
