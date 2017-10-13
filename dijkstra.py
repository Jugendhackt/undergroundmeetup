import numpy as np

#############
# CONSTANTS #
#############

INFINITY = float('inf')
UNDEFINED = None

######################
# DIJKSTRA ALGORITHM #
######################

# Find the point best to meet at for people at P1 and P2
# where data is the relationship matrix (numpy matrix) and 
# P1/P2 are the indices of the stations in the matrix (From Column to Row)
def findMeetPoint(data, P1, P2):
    data = np.array(data);
    vertices = np.array(range(0, data.shape[0]));
    dist = {};
    prev = {};

    for vertex in vertices:
        dist[vertex] = INFINITY;
        prev[vertex] = UNDEFINED;

    dist[P1] = 0;

    while (len(vertices) > 0): #while there are nodes left in the unknown set "Q"
        current_vertex = min(vertices, key=lambda x: dist[vertex]) #closest neighbor
        vertices = [] if len(vertices)==1 else vertices[vertices!=current_vertex]; #remove the node from the unknown set "Q"
        print(current_vertex);
        #Now iterate over all connections departing current_vertex except itself (remove -1 connections)
        for neighbor in [key for key in range(0, data.shape[0]) if key!=current_vertex and data[:, current_vertex][key]!=-1]:
            alt = dist[current_vertex] + data[current_vertex, neighbor];
            if (alt < dist[neighbor]): #If new route is better, change it
                dist[neighbor] = alt;
                prev[neighbor] = current_vertex;

    return prev;
            #   A   B   C   D   E (FROM)
test_graph = [[ 0,  1, -1,  8, -1], #Fastest path [AE] is A-B-C-D-E [WANTED]
              [ 1,  0,  2, -1, -1], #Shortest path [AE] is A-D-E
              [-1,  2,  0,  1,  4],
              [ 8, -1,  1,  0,  1],
              [-1, -1,  4,  1,  0]]

print(findMeetPoint(test_graph, 0, 4)) #Find fastest path for [AE] and print it