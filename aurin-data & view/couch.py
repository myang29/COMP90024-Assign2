import couchdb
from couchdb import design
#couchdb
user = "admin"
password = ""
couchserver = couchdb.Server("http://172.26.38.75:9024/")
# couchserver = couchdb.Server("http://%s:%s@115.146.92.83:8023/" % (user, password))



def upload(db_name, doc):
    if db_name in couchserver:
        db = couchserver[db_name]
    else:
        db = couchserver.create(db_name)
    doc_id, doc_rev = db.save(doc)


def createview(db_name, design_name, view_name, mapfunc, reducefuc):
    if db_name in couchserver:
        db = couchserver[db_name]
        print('db exist')
    else:
        db = couchserver.create(db_name)
        print('db NOT exist')

    view = design.ViewDefinition(
        '_design/'+design_name,                 #design document
        view_name,                        #view name
        mapfunc,                      #map
        reduce_fun = reducefuc)
    print (view.sync(db))



