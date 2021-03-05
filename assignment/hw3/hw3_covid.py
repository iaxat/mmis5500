# HW 3 Python
# Python Advance

# requests for data extract from API
import requests
import json
from datetime import date

# date time imported for creating date object
# json imported for writing json files

# covid function to run the program
# procedural programming used
def covid(country, status):
    req_dict = {}  # this to take request
    data_list = {}  # datalist for running analysis
    req_dict_json_file = {}  # this for writing to json file
    # dict created for saving data to be used later on

    countryStats = requests.get(
        f"https://covid-api.mmediagroup.fr/v1/history?country={country}&status={status}"
    ).json()
    req_dict = countryStats

    key1 = "All"
    key2 = "dates"
    # these keys for selecting data

    data_list = []

    # this is from creating list for analysis
    for key, value in req_dict[key1][key2].items():
        key = date.fromisoformat(key)
        if key >= date.fromisoformat("2020-02-15") and key <= date.fromisoformat(
            "2021-02-15"
        ):
            data_list.append([key, value])

    # this is for creating json file
    for key, value in req_dict[key1][key2].items():
        key_object = date.fromisoformat(key)
        if key_object >= date.fromisoformat(
            "2020-02-16"
        ) and key_object <= date.fromisoformat("2021-02-15"):
            req_dict_json_file[key] = value

    for i in range(0, len(data_list) - 1):
        data_list[i][1] = data_list[i][1] - data_list[i + 1][1]

    data_list.pop()

    # variables for the analysis
    # the dict for saving data
    sum = 0
    max_case = 0
    max_date = ""
    min_date = ""
    month_dict = {
        "Feb2020": 0,
        "Mar2020": 0,
        "Apr2020": 0,
        "May2020": 0,
        "Jun2020": 0,
        "Jul2020": 0,
        "Aug2020": 0,
        "Sep2020": 0,
        "Oct2020": 0,
        "Nov2020": 0,
        "Dec2020": 0,
        "Jan2021": 0,
        "Feb2021": 0,
    }
    for i in data_list:
        sum = sum + i[1]
        if i[1] >= max_case:
            max_case = i[1]
            max_date = i[0]
        if i[1] == 0 and min_date == "":
            min_date = i[0]
        if i[0].month == 2:
            if i[0].year == 2020:
                month_dict["Feb2020"] += i[1]
            else:
                month_dict["Feb2021"] += i[1]

        if i[0].month == 3:
            month_dict["Mar2020"] += i[1]

        if i[0].month == 4:
            month_dict["Apr2020"] += i[1]

        if i[0].month == 5:
            month_dict["May2020"] += i[1]

        if i[0].month == 6:
            month_dict["Jun2020"] += i[1]

        if i[0].month == 7:
            month_dict["Jul2020"] += i[1]

        if i[0].month == 8:
            month_dict["Aug2020"] += i[1]

        if i[0].month == 9:
            month_dict["Sep2020"] += i[1]

        if i[0].month == 10:
            month_dict["Oct2020"] += i[1]

        if i[0].month == 11:
            month_dict["Nov2020"] += i[1]

        if i[0].month == 12:
            month_dict["Dec2020"] += i[1]

        if i[0].month == 1:
            month_dict["Jan2021"] += i[1]
    # the conditions in here are for checking and putting in values

    # data saved in here
    # string variables for saving month and year
    max_month_cases = 0
    max_month = ""
    min_month_cases = 9999999999999
    min_month = ""
    # finding min and max
    for key, value in month_dict.items():
        if value < min_month_cases:
            min_month_cases = value
            min_month = key
        if value > max_month_cases:
            max_month_cases = value
            max_month = key

    # file name and writing to file
    # req_dict_json_file is the dict used to write data
    file_name = country
    with open(file_name + ".json", "w") as outfile:
        json.dump(req_dict_json_file, outfile)

    # console output
    print("\n")
    print("Covid Confirmed Cases Statistics")
    print("Country Name: ", country)
    print(
        "Average number of new daily confirmed cases for the year: ",
        sum / len(data_list),
    )
    print("Date with the highest new number of confirmed cases: ", max_date)
    print("Most recent date with no new confirmed cases: ", min_date)
    print(
        "Month with the highest new number of confirmed cases: ",
        max_month,
        ":",
        max_month_cases,
    )
    print(
        "Month with the lowest new number of confirmed cases: ",
        min_month,
        ":",
        min_month_cases,
    )


# loop to run all the 3 countries at once
countries = ["US", "China", "Germany"]
for i in countries:
    covid(i, "confirmed")
