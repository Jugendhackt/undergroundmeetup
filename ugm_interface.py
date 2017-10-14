import numpy as np
import csv
from ugm_algorithms import findMeetPoint

header = open('data.csv').readline().split(";")
data = np.loadtxt(open("data.csv", "rb"), delimiter=";", skiprows=1).transpose(1, 0)
print(data[1][0])
print(data.shape)
print(len(header))
locations = [14, 18]
print("Finding meeting point for:")
for station in locations:
    print(" - " + str(header[station]))
print("=> Meeting point: " + str(header[int(findMeetPoint(data, locations))]))