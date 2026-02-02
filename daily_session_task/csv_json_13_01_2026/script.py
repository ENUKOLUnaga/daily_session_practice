"""
Getting the data from csv file and filtering the data and storing in json file
"""

import csv
import json

battery_ranges = [
    (0, 10), (10, 20), (20, 30), (30, 40), (40, 50),
    (50, 60), (60, 70), (70, 80), (80, 90), (90, 100)
]
#reading data from csv
data_list = []
with open(r'E:\projects\Eco-Ride\data\fleet_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            row['ID'] = int(row['ID'])
            row['Battery'] = float(row['Battery'])
            data_list.append(row)
        except ValueError:
            continue 
data_list.sort(key=lambda x: x['ID'])
battery_data = {}
for start, end in battery_ranges:
    battery_data[str(start) + "-" + str(end)] = []
for item in data_list:
    battery = item['Battery']
    key = None
    for start, end in battery_ranges:
        if start <= battery < end:
            key = str(start) + "-" + str(end)
            break
    if battery == 100:
        key = "90-100"
    if key:
        battery_data[key].append(item)
#writing the data into json based battery range 
with open("filtered_data.json", "w") as jsonfile:
    json.dump(battery_data, jsonfile, indent=4)
