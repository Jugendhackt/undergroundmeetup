import numpy as np

#All Matricies are expected to be comlumn majour

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

    while (len(vertices)): #while there are nodes left in the unknown set "Q"
        current_vertex = min(vertices, key=lambda x: dist[vertex]) #closest neighbor
        vertices = [] if len(vertices)==1 else vertices[vertices!=current_vertex]; #remove the node from the unknown set "Q"
        print(current_vertex);
        #Now iterate over all connections departing current_vertex except itself (remove -1 connections)
        for neighbor in [key for key in range(0, data.shape[0]) if key!=current_vertex and data[:, current_vertex][key]!=-1]:
            alt = dist[current_vertex] + data[current_vertex, neighbor];
            if (alt < dist[neighbor]): #If new route is better, change it
                dist[neighbor] = alt;
                prev[neighbor] = current_vertex;

    return prev



#######################
# MEETPOINT ALGORITHM #
#######################

# Find the point best to meet at for people at P1 and P2
# where data is the relationship matrix (numpy matrix) and 
# P1/P2 are the indices of the stations in the matrix (From Column to Row)
def findMeetPoint(data, positions):
    data = np.array(data);
    vertices = [np.array(range(0, data.shape[0]))] * len(positions);
    knownPoints = [[]] * len(positions);
    prev = np.zeros( (len(positions), data.shape[0]) );
    dist = np.zeros( (len(positions), data.shape[0]) );

    for psn in range(0, len(positions)):
        for vertex in vertices[psn]:
            dist[psn][vertex] = INFINITY;
            prev[psn][vertex] = UNDEFINED;
        dist[psn][positions[psn]] = 0;

    while (len(min(vertices, key=lambda x: len(x))) > 0): #The algorithm will terminate eventually
        for psn in range(0, len(positions)):
            min_dist = min([v for k,v in np.ndenumerate(dist[psn]) if k in vertices[psn]]);
            current_vertices = [v for (k,v) in np.ndenumerate(vertices[psn]) if dist[psn][v] == min_dist];
            #current_vertices <- all vertices for [psn] with min dist[psn][i]
            for current_vertex in current_vertices:
                vertices[psn] = [] if len(vertices[psn])==1 else vertices[psn][vertices[psn]!=current_vertex]; #remove the node from the unknown set "Q"
                knownPoints[psn] = np.append(knownPoints[psn], current_vertex); #add node to known set

                #Now iterate over all connections departing current_vertex except itself (remove -1 connections)
                neighbors = [key for key in range(0, data.shape[0]) 
                                    if key!=current_vertex and data[:, current_vertex][key]!=-1]
                for neighbor in neighbors:
                    cur_dist = dist[psn][current_vertex];
                    neighbor_distance = data[current_vertex, neighbor];
                    alt = cur_dist + neighbor_distance;
                    if (alt < dist[psn][neighbor]): #If new route is better, change it
                        dist[psn][neighbor] = alt;
                        prev[psn][neighbor] = current_vertex;

        from functools import reduce
        knownIntersection = reduce(np.intersect1d, knownPoints)
        if (len(knownIntersection) == 1): return knownIntersection[0];
        if (len(knownIntersection) > 1): return int(min(knownIntersection, key=lambda x: max(dist[:,int(x)])));
    return -1;
            #   A   B   C   D   E (FROM)
#test_graph = [[ 0,  1, -1,  8, -1], #Fastest path [AE] is A-B-C-D-E [WANTED]
#              [ 1,  0,  2, -1, -1], #Shortest path [AE] is A-D-E
#              [-1,  2,  0,  1,  4],
#              [ 8, -1,  1,  0,  1],
#              [-1, -1,  4,  1,  0]]
#
#print(findMeetPoint(test_graph, [0, 2, 0])) #Find fastest path for [AE] and print it