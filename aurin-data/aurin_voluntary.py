import json
import couch

# process key data
with open('GCCSA_voluntary.json') as f:
    data = f.read()
f.close()

#parse json data
obj = json.loads(data)

# unwrap the json
list = obj['features']
print(len(list))

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

    # unwrapping, each 'doc' is a set of data for a region
    region_data = item['properties']
    # print(region_data)

    #process data
    gccsa_code = region_data['gcc_code16']
    if gccsa_code in GCCSA_map:
        new_doc = {}
        gcc_name = GCCSA_map[gccsa_code]

        total_person = region_data['p_total_total']
        volunteers = region_data['p_tot_volunteer']

        new_doc['gcc_code'] = gccsa_code
        new_doc['gcc_name'] = gcc_name
        new_doc['total_person'] = total_person
        new_doc['total_volunteers'] = volunteers
        new_doc['v_rate'] = round(volunteers/total_person, 5)

        couch.upload("gccsa_voluntary", new_doc)
        print(new_doc)