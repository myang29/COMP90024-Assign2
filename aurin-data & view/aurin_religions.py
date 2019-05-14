import json
import religionMap
import couch

# process key data
with open('GCCSA_religion.json') as f:
    religiondata = f.read()
f.close()

#parse json data
obj = json.loads(religiondata)

# unwrap the json
list = obj['features']
print(len(list))

#prepare a list for new docs
list_new_docs = []
GCCSA_map = {
    "1GSYD":"Sydney",
    "2GMEL":"Melbourne",
    "3GBRI":"Brisbane",
    "4GADE":"Adelaide",
    "5GPER":"Perth",
    "6GHOB":"Hobart",
    "7GDAR":"Darwin",
    "8ACTE":"Canberra"
}

for item in list:

    # unwrapping, each 'doc' is a set of data for an SA2 region
    region_data = item['properties']
    # print(region_data)

    #process other data (which are not person number of a religion)
    gcc_code = region_data.pop('gcc_code16')
    if gcc_code in GCCSA_map:
        total_person = region_data.pop('tot_p')
        region_data.pop('gcc_name16')
        gcc_name = GCCSA_map[gcc_code]
        new_region_doc = {}

        # construct new doc
        new_region_doc['gcc_code'] = gcc_code
        new_region_doc['total_person'] = total_person
        new_region_doc['gcc_name'] = gcc_name

        # check if there is data for the region
        dataNotNull = bool(total_person > 50)

        # record the religion with biggest number of persons
        max_religion_person = 0
        max_religion = 'null'
        max_religion_title = 'null'

        # process each religion in the region
        for religion in region_data:

            # # compare with the max
            # if dataNotNull and person > max_religion_person:
            #     max_religion_person = person
            #     max_religion = religion
            #     max_religion_title = title

            # compute percentage
            percentage = round(float(region_data[religion])/ (total_person if dataNotNull else 1), 5)
            if religion == 'sb_osb_nra_nr_p':
                no_religion = percentage
            if religion == 'religious_affiliation_ns_p':
                religion_not_stated = percentage


            # add to new dict
            title = religionMap.attribute_map[religion]
            new_region_doc[title] = percentage

        # compute the max religion's percentage

        # max_religion_percentage = new_region_doc[max_religion] if dataNotNull else 0

        # add max religion's data to doc
        # new_region_doc['max_religion'] = max_religion
        # new_region_doc['max_religion_percentage'] = max_religion_percentage
        # new_region_doc['max_religion_person'] = max_religion_person
        # new_region_doc['max_religion_title'] = max_religion_title

        # check if the max religion has children
        # if max_religion in religionMap.parent_key:

            # children = religionMap.parent_child_dict[max_religion]

            # construct child/parent percentage data for the max religion
            # child_percentage_data = {}
            # for child in children:
            #     child_percent = new_region_doc[child]
            #     parent_percent = max_religion_percentage
            #     child_percentage_data[child] = round(child_percent / parent_percent, 5)

        # compute religious percentage
        religious_percent = round(1 - no_religion - religion_not_stated, 5)
        new_region_doc['religious_percent'] = religious_percent


        # add it to the doc
        # new_region_doc['max_relig_child_percent_data'] = child_percentage_data

        # send doc to couchdb server
        couch.upload("gccsa_religion", new_region_doc)
        # print(new_region_doc)



    # list_new_docs.append(new_region_doc)
    # print(list_new_docs)


