# BellmanFord Algorithm - Finding shortest Path with graph having negative edges

''' 
The Bellman-Ford algorithm is used to find the shortest paths from a source node to all other nodes in a graph. 
Unlike Dijkstra’s algorithm, it works with graphs that have negative weight edges. 
*** However, it cannot handle graphs with negative weight cycles (cycles whose total weight is negative).

Steps of the Algorithm:
1 . Initialize Distances:

	Create a distance array and initialize the distance to all nodes as infinity (∞), except for the source node, which is set to 0.

2 . Relax All Edges Repeatedly:

	For each edge in the graph, update the distance to the target node if the current path is shorter than the known distance.
	Repeat this for all edges (V−1) times, where 𝑉 is the number of nodes.

3 . Check for Negative Weight Cycles:

	Perform one more pass over all edges.
	If any distance can still be updated, the graph contains a negative weight cycle.

'''
from typing import List, Tuple

def bellman_ford(V: int, edges: List[Tuple[int, int, int]], src: int) -> List[float]:
    # Step 1: Initialize distances from the source
    distances = [float('inf')] * V
    distances[src] = 0

    # Step 2: Relax edges V-1 times
    for _ in range(V - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Step 3: Check for negative weight cycles
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle")
            return []

    return distances

# Example usage
if __name__ == "__main__":
    V = 5
    edges1 = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    edges2 = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 3, 5),
        (3, 4, 3),
        (4, 3, -6)  # Negative weight cycle example
    ]
    src = 0
    distances1 = bellman_ford(V, edges1, src)
    distances2 = bellman_ford(V, edges2, src)
    print("Shortest distances from source vertex", src, ":", distances1)
    print("Shortest distances from source vertex", src, ":", distances2)