import couchdb

address = "http://115.146.92.83:8022"

couch = couchdb.Server(address)

db = couch['processed_twit']


for id in db:
    doc = db.get(id)
    doc['_id'] = str(doc['id'])
    db.save(doc)