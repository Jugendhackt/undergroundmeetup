import numpy as np

#############
# CONSTANTS #
#############

INFINITY = float('inf')
UNDEFINED = None



######################
# DIJKSTRA ALGORITHM #
######################

# Classical dijkstra implementation
# searching for the fastest route from P1 to P2
# where data is the relationship matrix (numpy matrix) and 
# P1/P2 are the indices of the stations in the matrix (From Column to Row)
def dijkstra(data, P1, P2):
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



#######################
# MEETPOINT ALGORITHM #
#######################

# Find the point best to meet at for people at P1 and P2
# where data is the relationship matrix (numpy matrix) and 
# P1/P2 are the indices of the stations in the matrix (From Column to Row)
def findMeetPoint(data, P1, P2):
    #Suffix _P: P1 -> P2
    #Suffix _M: P2 -> P1
    data = np.array(data);
    vertices_P = np.array(range(0, data.shape[0]));
    vertices_M = np.array(range(0, data.shape[0]));
    knownPoints_P = [];
    knownPoints_M = [];
    dist_P = {};
    prev_P = {};
    dist_M = {};
    prev_M = {};


    for vertex in vertices_P:
        dist_P[vertex] = INFINITY;
        prev_P[vertex] = UNDEFINED;
    for vertex in vertices_M:
        dist_M[vertex] = INFINITY;
        prev_M[vertex] = UNDEFINED;

    dist_P[P1] = 0;
    dist_M[P2] = 0;

    while (len(vertices_P) > 0 and len(vertices_M) > 0): #while there are nodes left in the unknown set "Q"
        current_vertex_P = min(vertices_P, key=lambda x: dist_P[x]) #closest neighbor
        current_vertex_M = min(vertices_M, key=lambda x: dist_M[x])
        vertices_P = [] if len(vertices_P)==1 else vertices_P[vertices_P!=current_vertex_P]; #remove the node from the unknown set "Q"
        vertices_M = [] if len(vertices_M)==1 else vertices_M[vertices_M!=current_vertex_M];
        knownPoints_P = np.append(knownPoints_P, current_vertex_P);
        knownPoints_M = np.append(knownPoints_M, current_vertex_M);

        #Now iterate over all connections departing current_vertex except itself (remove -1 connections)
        for neighbor in [key for key in range(0, data.shape[0]) if key!=current_vertex_P and data[:, current_vertex_P][key]!=-1]:
            alt = dist_P[current_vertex_P] + data[current_vertex_P, neighbor];
            if (alt < dist_P[neighbor]): #If new route is better, change it
                dist_P[neighbor] = alt;
                prev_P[neighbor] = current_vertex_P;

        for neighbor in [key for key in range(0, data.shape[0]) if key!=current_vertex_M and data[:, current_vertex_M][key]!=-1]:
            alt = dist_M[current_vertex_M] + data[current_vertex_M, neighbor];
            if (alt < dist_M[neighbor]): #If new route is better, change it
                dist_M[neighbor] = alt;
                prev_M[neighbor] = current_vertex_M;

        knownIntersection = np.intersect1d(knownPoints_P, knownPoints_M);
        if (len(knownIntersection) > 0): return knownIntersection;

    return -1;
            #   A   B   C   D   E (FROM)
test_graph = [[ 0,  1, -1,  8, -1], #Fastest path [AE] is A-B-C-D-E [WANTED]
              [ 1,  0,  2, -1, -1], #Shortest path [AE] is A-D-E
              [-1,  2,  0,  1,  4],
              [ 8, -1,  1,  0,  1],
              [-1, -1,  4,  1,  0]]

print(findMeetPoint(test_graph, 0, 4)) #Find fastest path for [AE] and print it