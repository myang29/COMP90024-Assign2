import json
import couch

# process key data
with open('volun_age.json') as f:
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

        #location data
        new_doc['gcc_code'] = gccsa_code
        new_doc['gcc_name'] = gcc_name

        #total data
        total_person = region_data['p_total_total']
        total_volunteers = region_data['p_tot_volunteer']

        #different age data
        total_15_19 = region_data['p_15_19_yr_total']
        new_doc['total_15_19'] = total_15_19
        volun_15_19 = region_data['p_15_19_yr_volunteer']
        new_doc['volun_15_19'] = volun_15_19
        new_doc['rate_15_19'] = round(float(volun_15_19)/total_15_19, 5)

        total_20_24 = region_data['p_20_24_yr_total']
        new_doc['total_20_24'] = total_20_24
        volun_20_24 = region_data['p_20_24_yr_volunteer']
        new_doc['volun_20_24'] = volun_20_24
        rate_20_24 = round(float(volun_20_24) / total_20_24, 5)
        new_doc['rate_20_24'] = rate_20_24

        total_25_34 = region_data['p_25_34_yr_total']
        new_doc['total_25_34'] = total_25_34
        volun_25_34 = region_data['p_25_34_yr_volunteer']
        new_doc['volun_25_34'] = volun_25_34
        rate_25_34 = round(float(volun_25_34) / total_25_34, 5)
        new_doc['rate_25_34'] = rate_25_34

        total_35_44 = region_data['p_35_44_yr_total']
        new_doc['total_35_44'] = total_35_44
        volun_35_44 = region_data['p_35_44_yr_volunteer']
        new_doc['volun_35_44'] = volun_35_44
        rate_35_44 = round(float(volun_35_44) / total_35_44, 5)
        new_doc['rate_35_44'] = rate_35_44

        total_45_54 = region_data['p_45_54_yr_total']
        new_doc['total_45_54'] = total_45_54
        volun_45_54 = region_data['p_45_54_yr_volunteer']
        new_doc['volun_45_54'] = volun_45_54
        rate_45_54 = round(float(volun_45_54) / total_45_54, 5)
        new_doc['rate_45_54'] = rate_45_54

        total_55_64= region_data['p_55_64_yr_total']
        new_doc['total_55_64'] =total_55_64
        volun_55_64= region_data['p_55_64_yr_volunteer']
        new_doc['volun_55_64'] =volun_55_64
        rate_55_64= round(float(volun_55_64) / total_55_64, 5)
        new_doc['rate_55_64'] =rate_55_64

        total_65_74 = region_data['p_65_74_yr_total']
        new_doc['total_65_74'] = total_65_74
        volun_65_74 = region_data['p_65_74_yr_volunteer']
        new_doc['volun_65_74'] = volun_65_74
        rate_65_74 = round(float(volun_65_74) / total_65_74, 5)
        new_doc['rate_65_74'] = rate_65_74

        total_75_84 = region_data['p_75_84_yr_total']
        new_doc['total_75_84'] =total_75_84
        volun_75_84 = region_data['p_75_84_yr_volunteer']
        new_doc['volun_75_84'] = volun_75_84
        rate_75_84 = round(float(volun_75_84) / total_75_84, 5)
        new_doc['rate_75_84'] = rate_75_84

        total_over_85= region_data['p_85_yr_over_tot']
        new_doc['total_over_85'] = total_over_85
        volun_over_85 = region_data['p_85_yr_over_volunteer']
        new_doc['volun_over_85'] = volun_over_85
        rate_over_85 = round(float(volun_over_85) / total_over_85, 5)
        new_doc['rate_over_85'] = rate_over_85

        #total voluntary percentage
        new_doc['total_person'] = total_person
        new_doc['total_volunteers'] = total_volunteers
        new_doc['v_rate'] = round(total_volunteers/total_person, 5)

        couch.upload("gccsa_voluntary", new_doc)
        print(new_doc)