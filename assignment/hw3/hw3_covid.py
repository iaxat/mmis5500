# HW 3 for Python 5500 Course
# COVID Study

import requests
from os import path
import time
import json

def append(ticker):
    url = (
"https://covid-api.mmediagroup.fr/v1/cases"
    )
    req = requests.get(url)
    time.sleep(13)
    # sleep is required or else the api key will max out its ability to send data

    req_dict = json.loads(req.text)
    # the load funtion takes the text encoding format and makes a dictionary out of it
    print(req_dict.keys())
    # this will print the keys of the dict which can help determine the keys to be used in json file filter process

    key1 = "Time Series (Daily)"  # dictionary with all prices by date
    key2 = "4. close"
    # the keys to be used to define and filter the jscon file and derive what is fruitful for the project
    # the below csv file is onlu possible after the keys are identified and the appropriate data is identified
    csv_file = open(ticker + ".csv", "r")
    lines = csv_file.readlines()
    last_date = lines[-1].split(",")[0]
    # last date checks if there is any latest data that needs to be appended
    new_lines = []
    # new lines is for creating the array with new data that needs to be appeneded in already created file
    for date in req_dict[key1]:
        if date == last_date:
            break
        print(date + "," + req_dict[key1][date][key2])  # print key, value
        new_lines.append(date + "," + req_dict[key1][date][key2] + "\n")

    # new lines is used here to make the whole series of data in an well arranged order to be used by the algorithms
    new_lines = new_lines[::-1]
    # Enter the directory
    csv_file = open(
        "Enter the Directory Here" + ticker + ".csv", "a"
    )  # opening the file to append data
    csv_file.writelines(new_lines)  # appending new data
    csv_file.close()

    # Return the CSV file for further usage
    return csv_file
    # function ends here


def process_json(ticker):
    # this function is used in a situation where the ticker file does not exist
    # this fucntion creates a file in the scenario the user puts the ticker name & is not present to the algorithms for analysis
    # in that scenario using the api this function will gather all the dat and create a file and make it available for analysis
    url = (
        "http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
        + ticker
        + "&outputsize=full&apikey="
        + API_KEY
    )
    req = requests.get(url)
    time.sleep(13)

    req_dict = json.loads(req.text)

    print(req_dict.keys())

    key1 = "Time Series (Daily)"  # dictionary with all prices by date
    key2 = "4. close"
    # the keys will help seperate and help in filter of the json file to create csv files

    csv_file = open(ticker + ".csv", "w")
    csv_file.write("Date,AAPL\n")
    # file writing process
    write_lines = []
    for date in req_dict[key1]:
        print(date + "," + req_dict[key1][date][key2])  # print key, value
        write_lines.append(date + "," + req_dict[key1][date][key2] + "\n")
    # algo to write data into the files
    # the keys inside are used to filte the data
    write_lines = write_lines[::-1]
    csv_file.writelines(write_lines)
    csv_file.close()

    # this will make the function csv file created for the analysis
    return csv_file