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

file_lines = open('tokyo-metro-data/lines.csv')
for line in file_lines:
    prefix  = line.split(';')[0]
    start   = int(line.split(';')[1])
    end     = int(line.split(';')[2])
    times    = line.split(';')[3:]
    for i in range(start, end):
        stations.append(prefix + ("0" if i < 10 else "") + str(i))
        relations.append(StationRelation(prefix + ("0" if i < 10 else "") + str(i), 
                                         prefix + ("0" if i < 10 else "") + str(i), 
                                         0)) #0 for itself
        if (i != start):
            relations.append(StationRelation(
                             prefix + ("0" if i-1 < 10 else "") + str(i-1),
                             prefix + ("0" if i+0 < 10 else "") + str(i+0),
                             int(times[i - start])))

file_lines = open('tokyo-metro-data/transitions.csv')
for line in file_lines:
    prefix1  = line.split(';')[0]
    prefix2  = line.split(';')[2]
    number1  = line.split(';')[1]
    number2  = line.split(';')[3]
    time     = line.split(';')[4]
    relations.append(StationRelation(str(prefix1) + str(number1),str(prefix2) + str(number2), int(time)))

header_line = ""

for station in stations: 
    header_line += station + ";"

# Remove last simicolon from header line
header_line = header_line[:-1]

# Generate staion_size x station_size filled with -1's
matrix = np.ones(shape=(len(header_line), len(header_line))) * -1;

# Replace all relations in matix
for relation in relations:
    matrix[stations.index(relation.stationOne)][stations.index(relation.stationTwo)] = relation.stationTime;
    matrix[stations.index(relation.stationTwo)][stations.index(relation.stationOne)] = relation.stationTime;

# Write the matrix in csv format
output = open('data.generated.csv', "w+")
output.writelines(header_line)
output.write('\n')
for column in range(0, len(header_line) - 1):
    for row in range(0, len(header_line) - 1):
        output.write(str(matrix[column][row]))
        output.write(';' if row != len(header_line) else '')
    output.write('\n')
print("Done!")