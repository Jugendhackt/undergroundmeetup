import numpy as np
from functools import reduce

# All Matricies are expected to be comlumn majour

#############
# CONSTANTS #
#############

INFINITY = float('inf')
UNDEFINED = None

######################
# DIJKSTRA ALGORITHM #
######################


def dijkstra(data, P1, P2):
    """
    Classical dijkstra implementation
    searching for the fastest route from P1 to P2
    where data is the relationship matrix (numpy matrix) and
    P1/P2 are the indices of the stations in the matrix (From Column to Row)
    """
    data = np.array(data)
    vertices = np.array(range(0, data.shape[0]))
    dist = {}
    prev = {}

    for vertex in vertices:
        dist[vertex] = INFINITY
        prev[vertex] = UNDEFINED

    dist[P1] = 0

    while (len(vertices)):  # while there are nodes left in the unknown set "Q"
        # closest neighbor
        current_vertex = min(vertices, key=lambda x: dist[vertex])
        if len(vertices) == 1:
            vertices = []
        else:
            # remove the node from the unknown set "Q"
            vertices[vertices != current_vertex]

        # Now iterate over all connections departing
        # current_vertex except itself (remove -1 connections)
        for neighbor in [key for key in range(0, data.shape[0])
                         if key != current_vertex and
                         data[:, current_vertex][key] != -1]:
            alt = dist[current_vertex] + data[current_vertex, neighbor]
            if (alt < dist[neighbor]):  # If new route is better, change it
                dist[neighbor] = alt
                prev[neighbor] = current_vertex

    return prev

#######################
# MEETPOINT ALGORITHM #
#######################


def findMeetPoint(data, positions):
    """
    Find the point best to meet at for people at P1 and P2
    where data is the relationship matrix (numpy matrix) and
    P1/P2 are the indices of the stations in the matrix (From Column to Row)
    """
    data = np.array(data)
    vertices = [np.array(range(0, data.shape[0]))] * len(positions)
    knownPoints = [[]] * len(positions)
    prev = np.zeros((len(positions), data.shape[0]))
    dist = np.zeros((len(positions), data.shape[0]))

    for psn in range(0, len(positions)):
        for vertex in vertices[psn]:
            dist[psn][vertex] = INFINITY
            prev[psn][vertex] = UNDEFINED
        dist[psn][positions[psn]] = 0

    while (len(min(vertices, key=lambda x: len(x))) > 0):
        for psn in range(0, len(positions)):
            min_dist = min([v for k, v in np.ndenumerate(dist[psn])
                            if k in vertices[psn]])
            current_vertices = [v for k, v in np.ndenumerate(vertices[psn])
                                if dist[psn][v] == min_dist]

            # current_vertices <- all vertices for [psn] with min dist[psn][i]
            for current_vertex in current_vertices:
                if len(vertices[psn]) == 1:
                    vertices[psn] = []
                else:
                    # remove the node from the unknown set "Q"
                    vertices[psn][vertices[psn] != current_vertex]

                knownPoints[psn] = np.append(knownPoints[psn], current_vertex)

                # Now iterate over all connections departing current_vertex
                # except itself (remove -1 connections)

                # Column Majour:
                departures = data[current_vertex, :]
                neighbors = [key for key in range(0, data.shape[0])
                             if key != current_vertex and
                             departures[key] != -1]

                for neighbor in neighbors:
                    cur_dist = dist[psn][current_vertex]
                    neighbor_distance = data[current_vertex, neighbor]
                    if (neighbor_distance < 1):
                        raise Exception("Data corrupted at (" +
                                        str(current_vertex) + "|" +
                                        str(neighbor) + ")!")
                    alt = cur_dist + neighbor_distance
                    # If new route is better, change it
                    if (alt < dist[psn][neighbor]):
                        dist[psn][neighbor] = alt
                        prev[psn][neighbor] = current_vertex

        knownIntersection = reduce(np.intersect1d, knownPoints)
        if (len(knownIntersection) == 1):
            return knownIntersection[0]
        if (len(knownIntersection) > 1):
            return int(min(knownIntersection,
                       key=lambda x: max(dist[:, int(x)])))
    return -1
