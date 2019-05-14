import json
import diseaseMap
import re
import couch

# process key data
with open('diseasedata.json') as f:
    diseasedata = f.read()
f.close()

#parse json data
obj = json.loads(diseasedata)

# unwrap the json
list = obj['features']
print(len(list))

for region in list:

    # unwrapping, each 'doc' is a set of data for an SA2 region
    region_data = region['properties']

    # process other data (which are not person number of a religion)
    SA2_code = region_data.pop('area_code')
    SA2_name = region_data.pop('area_name')

    # construct new doc
    new_region_doc = {}
    new_region_doc['SA2_code'] = SA2_code
    new_region_doc['sa2_name16'] = SA2_name

    # record the religion with the highest rate/count
    max_disease_count = 0
    max_disease_rate = 0
    max_disease = ""
    diseaseRate = {}
    diseaseCount = {}
    # process each religion in the region
    for key in region_data:

        if str(key).find("_no_") > -1:
            #it is a count
            disease = diseaseMap.attribute_map[key]
            disease =re.sub(' - Count','',disease)
            diseaseCount[disease] = region_data[key]
        elif str(key).find("_rate_") >-1:
            #it is a rate
            disease = diseaseMap.attribute_map[key]
            disease = re.sub(' - Rate per 100', '', disease)
            diseaseRate[disease] = region_data[key]
        # elif str(key).find("_rrmse") >-1:
            #it is a rrmse

    # filter according to RRMSE
    # reliableDataDisease = []
    # for disease in diseaseRRMSE:
    #     rrmse = diseaseRRMSE[disease]
    #     if (rrmse!= None) and (rrmse < 2):
    #         reliableDataDisease.append(disease)
    #

    # find the max rate disease
    for disease in diseaseRate:
        # if disease in reliableDataDisease:
            rate = diseaseRate[disease]
            new_region_doc[disease] = diseaseRate[disease]
            if (rate != None) and (rate > max_disease_rate):
                max_disease = disease
                max_disease_rate = rate
                max_disease_count = diseaseCount[disease]



    # #add to region dict
    new_region_doc['max_disease'] = max_disease
    new_region_doc['max_disease_rate'] = max_disease_rate
    new_region_doc['max_disease_count'] = max_disease_count

    print (new_region_doc)

    # send doc to couchdb server
    couch.upload("aurin_disease", new_region_doc)