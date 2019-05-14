import json
import re
import couch

#create a map for attributes
with open('GCCSA_religion_meta.json') as f:
    religionmeta = f.read()

obj = json.loads(religionmeta)
list = obj['selectedAttributes']  # unwrapping

#for religion classification
parent_key = ['buddhism_p',
              'christianity_tot_p',
              'hinduism_p',
              'islam_p',
              'judaism_p',
              'other_religions_tot_p',
              'religious_affiliation_ns_p',
              'sb_osb_nra_tot_p']
not_religion_key = ['tot_p',
                'gcc_code16',
                'gcc_name16']

attribute_map = {}

#add parents to map
for item in list:
    key = item['name']
    title = item['title']
    if key in parent_key:
        title = title = re.sub(' Persons', '', item['title'])
        attribute_map[key] = title


parent_child_dict = {}
for p_key in parent_key:
    parent_child_dict[p_key] = []


#process and add children to map
for item in list:
    c_key = item['name']
    c_title = item['title']

    #only process children
    if (c_key not in parent_key) & (c_key not in not_religion_key):
        c_title = re.sub(' Persons', '', item['title'])

        #look for the according parent
        for p_key in parent_key:
            p_title = attribute_map[p_key]
            p_title = re.sub(' Total', '', p_title)
            if c_title.find(p_title) > -1:

                #add relationship to dict
                parent_child_dict[p_key].append(c_key)

                #modify title
                c_title = re.sub(p_title,'',c_title)
                new_title = c_title.strip()

        #add the child to the map
        attribute_map[c_key] = new_title

# print(attribute_map)
couch.upload("religion_map", attribute_map)
couch.upload("religion_map", {'parent_child_dict':parent_child_dict})


# f = open("attribute_map.json","w")
# attribute_map_json = json.dump(attribute_map,f)
# f.write(str(attribute_map_json))
# f.close()