# Floyd - Warshall Algorithm : Dynamic Programming algorithm. 

''' 
It works for both directed and undirected graphs.
used to find the shortest paths between all pairs of vertices in a weighted graph.

Note: It can handle graphs with negative weights but does not work with negative weight cycles.

Steps:
1 . Convert Adjacency List to Distance Matrix:

	Create a distance matrix dist where dist[i][j] is initialized to:
	The weight of the edge from i to j (if it exists) else 0 if i=j and ∞ if there's no direct edge between i and j.

2 . Apply the Floyd-Warshall Algorithm:

	Use dynamic programming to update the shortest distances for all pairs of nodes.

3 . Detect Negative Cycles:

	Check the diagonal of the distance matrix. If any dist[i][i]<0, the graph contains a negative weight cycle.

'''
from collections import defaultdict
import math

def floyd_warshall_adj_list(adj_list, V):
    # Initialize distance matrix
    dist = [[float('inf')] * V for _ in range(V)]
    
    # Fill the matrix based on the adjacency list
    for u in range(V):
        dist[u][u] = 0  # Distance to itself is 0
    for u,v, weight in adj_list:
        dist[u][v] = weight
    
    # Apply Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Detect negative weight cycles
    for i in range(V):
        if dist[i][i] < 0:
            print("Graph contains a negative weight cycle")
            return None
    
    return dist

if __name__ == "__main__":
    edges = [
        [0, 1, 3],
        [0, 2, 5],
        [1, 2, 1],
        [2, 3, 2],
        [1, 3, 6]
    ]
    V = 5 
    result = floyd_warshall_adj_list(edges, V)
    
    if result:
        print("Shortest distance matrix:")
        for row in result:
            print(row)
