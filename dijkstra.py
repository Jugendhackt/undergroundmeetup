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
    vertices = range(1, data.shape.x);
    dist = {};
    prev = {};

    for vertex in vertices:
        dist[vertex] = INFINITY;
        prev[vertex] = UNDEFINED;

    dist[P1] = 0;

    while (vertices.length > 0): #while there are nodes left in the unknown set "Q"
        current_vertex = min(vertices, key=lambda x: dist[vertex]) #closest neighbor
        del vertices[current_vertex]; #remove the node from the unknown set "Q"

        #Now iterate over all connections departing current_vertex except itself (remove -1 connections)
        for neighbor in [x for i,x in enumerate(data[:, current_vertex]) if i!=current_vertex and x!=-1]
            alt = dist[current_vertex] + length(current_vertex, neighbor);
            if (alt < dist[neighbor]) #If new route is better, change it
                dist[neighbor] = alt;
                prev[neighbor] = current_vertex;

    return prev;