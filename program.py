import numpy as np
import csv, os
from mat4py import savemat

DATASET_INPUT = 'weatherAUS.csv'
DATASET_OUTPUT = 'dataset.mat'
LOCATIONS = "locations/"
DATASET_LOCATIONS = '_dataset.mat'

try:
    os.mkdir(LOCATIONS)
except:
    print("locations/ not created")

mat = []
location2mat = {}

with open(DATASET_INPUT, "rt",newline='') as input_file:
    reader = csv.DictReader(input_file, delimiter=',')
    for record in reader:
        location = record['Location']
        if not location in location2mat.keys():
            location2mat[location] = []
        
        try:
            row1 = [float(record['Humidity9am']),float(record['Pressure9am']),float(record['Temp9am'])]
            mat.append(row1)
            location2mat[location].append(row1)
        except:
            pass
        try:
            row2 = [float(record['Humidity3pm']),float(record['Pressure3pm']),float(record['Temp3pm'])]
            mat.append(row2)
            location2mat[location].append(row2)
        except:
            pass



savemat(DATASET_OUTPUT,{'D':mat})
for location in location2mat.keys():
    if location2mat[location] != []:
        name = LOCATIONS + location + DATASET_LOCATIONS
        print(name)
        savemat(name,{'D':location2mat[location]})