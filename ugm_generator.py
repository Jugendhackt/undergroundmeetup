# This script converts data.station.csv and data.lines.csv to 
# matrix graph like data.generated.csv data format.

##### DO NOT EDIT data.generated.csv #####

import numpy as np
import csv

class StationRelation:
    def __init__(self, stationOne, stationTwo, stationTime):
        self.stationOne = stationOne
        self.stationTwo = stationTwo
        self.stationTime = stationTime

stations = []
relations = []

file_lines = open('data.lines.csv')
for line in file_lines:
    prefix  = line.split(';')[0]
    start   = line.split(';')[1]
    end     = line.split(';')[2]
    times    = line.split(';')[3:]
    for i in range(start, end):
        stations.append(str(prefix) + str(i))
        if (i != offset) relations.append(str(prefix) + str(i-1),
                                        str(prefix) + str(i+0),
                                        int(times[i - start]))
print(stations)
print(relations)                                          