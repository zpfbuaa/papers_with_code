"""
To create output matrices dist and time that can give temporal and spatial distance from all to all nodes
run using:
python FloydWarshall.py <input file> <output file>
input file must adhere to the following format:
no. of nodes(V)
no. of arcs(E)
<tail node> <head node> <weight>                --this line occurs E times
"""

import sys
import numpy as np
from Driver import Driver

# recursive function to obtain the path as a string
def obtainPath(i, j):
    if dist[i][j] == float("inf"):
        return " no path to "
    if parent[i][j] == i:
        return " "
    else:
        return obtainPath(i, parent[i][j]) + str(parent[i][j]+1) + obtainPath(parent[i][j], j)

try:
    fil = open("edge_length.txt", "r")
except IOError:
    print("File not found.")
    sys.exit(-1)

# no of vertices
V = int(fil.readline().strip())
# array of shortest path distances
dist = []
# array of travel time of shortest path distances
time = []
# array of shortest paths
parent = []
# no of edges
E = int(fil.readline().strip())

# init with infinite distances
for i in range(0, V):
    dist.append([])
    parent.append([])
    time.append([])
    for j in range(0, V):
        dist[i].append(float("inf"))
        time[i].append(float("inf"))
        parent[i].append(0)

# read edges from input file and store
for i in range(0, E):
    t = fil.readline().strip().split()
    x = int(t[0]) - 1
    y = int(t[1]) - 1
    w = int(t[2])
    dist[x][y] = w
    parent[x][y] = x

# path from vertex to itself is set to 0
for i in range(0, V):
    dist[i][i] = 0

# initialize the path matrix
for i in range(0,V):
    for j in range(0,V):
        if dist[i][j] == float("inf"):
            parent[i][j] = 0
        else:
            parent[i][j] = i

# floyd warshall algorithm
for k in range(0, V):
    for i in range(0, V):
        for j in range(0, V):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                parent[i][j] = parent[k][j]

# cal the travel time
for i in range(V):
    for j in range(V):
        time[i][j] = dist[i][j] / Driver.speed

# display shortest paths
"""
for i in range(0,V):
    print
    for j in range(0,V):
        print("From:", i+i, "To:", j+1)
        print("Path:", str(i+1) + obtainPath(i,j) + str(j+1))
        print("Distance:", dist[i][j])
"""

# save output
np.savetxt("dist.txt", dist, fmt='%-3.0f')
np.savetxt("route.txt", parent, fmt='%-3d')
np.savetxt("time.txt", time, fmt='%-3.0f')

fil.close()