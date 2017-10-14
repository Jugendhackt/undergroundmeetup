import numpy as np
import csv
from ugm_algorithms import findMeetPoint

header = open('data.csv').readline().split(";")
data = np.loadtxt(open("data.csv", "rb"), delimiter=";", skiprows=1).transpose(1, 0)
print(data[1][0])
print(data.shape)
print(len(header))
locations = [0, 18, 14]
print("Finding meeting point for:")
for station in locations:
    print(" - " + str(header[station]))
print("=> Meeting point: " + str(header[int(findMeetPoint(data, locations))]))


            #   A   B   C   D   E (FROM)
#test_graph = [[ 0,  1, -1,  8, -1], #Fastest path [AE] is A-B-C-D-E [WANTED]
#              [ 1,  0,  2, -1, -1], #Shortest path [AE] is A-D-E
#              [-1,  2,  0,  1,  4],
#              [ 8, -1,  1,  0,  1],
#              [-1, -1,  4,  1,  0]]
#
#print(findMeetPoint(test_graph, [0, 2, 0])) #Find fastest path for [AE] and print it