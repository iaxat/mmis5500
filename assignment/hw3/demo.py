import requests
import json
from datetime import date

def covid(country, status):
    req_dict = {}
    req_dict_selected = {}
    temp_dict = {}
    countryStats = requests.get(f"https://covid-api.mmediagroup.fr/v1/history?country={country}&status={status}").json()
    req_dict = countryStats
    # stateStats = countryStats[status]
    # print([stateStats['confirmed'], stateStats['recovered'], stateStats['deaths']])

    key1 = "All"
    key2 = "dates"

    for key, value in req_dict[key1][key2].items():
        # print(key)
        # print(value)

        key_obj = date.fromisoformat(key)
        # print(key_obj,value)
        if key_obj >= date.fromisoformat('2020-02-16') and key_obj<= date.fromisoformat('2021-02-15'):
            req_dict_selected[key] = value    

    print(req_dict_selected)
    file_name = country
    with open(file_name+'.json', 'w') as outfile:
        json.dump(req_dict_selected, outfile)


        if key_obj >= date.fromisoformat('2020-02-1') and key_obj<= date.fromisoformat('2021-02-30'):
            req_dict_selected[key] = value 






countries = ["US","China","Germany"]
for i in countries:
    covid(i, "confirmed")