import requests
import json
from datetime import date

def append():
    req_dict={}
    url = (
"https://covid-api.mmediagroup.fr/v1/history?country=India&status=confirmed"
    )
    req = requests.get(url)
    req_dict = json.loads(req.text)
    dic_dates_india = req_dict['All']['dates']
    print(req_dict)
# append()


def covid(country, status):
    req_dict = {}
    req_dict_selected = {}
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

    with open('country.json', 'w') as outfile:
        json.dump(req_dict_selected, outfile)

covid("India", "confirmed")