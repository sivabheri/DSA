# Dijkstra's Algorithm - Finding Shorest path in any graph with non-negative edge weights.

''' 
Dijkstra’s Algorithm is used for solving single source shortest path problems.
Steps of Dijkstra's Algorithm:
1 .Initialize Distances:

	Create a distance array to store the shortest distance from the starting node to every other node.
	Set the distance of the starting node to 0 (because the distance to itself is zero) and all other nodes to infinity (∞).

2 . Use a Priority Queue:

	Use a priority queue (or a similar data structure) to always process the node with the smallest known distance.

3 . Process Each Node:

	Remove the node with the smallest distance from the priority queue.

	For each of its neighbors, calculate the distance through the current node:
	New Distance = Current Distance + Edge Weight.
	If this new distance is smaller than the previously known distance to the neighbor, update it in the distance array and add the neighbor to the queue.

4 . Repeat Until All Nodes Are Processed:

	Continue processing nodes until the priority queue is empty, which means all nodes have been visited with their shortest distances determined.

5 . Return the Results:

	Once the algorithm finishes, the distance array contains the shortest distances from the starting node to all other nodes.

'''
import heapq
from typing import List, Tuple

def dijkstra(V: int, edges: List[Tuple[int, int, int]], src: int) -> List[int]:
    
    # 1. Create an adjacency list
    graph = [[] for _ in range(V)]
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # For undirected graph

    # 2. Initialize distances and priority queue
    distances = [float('inf')] * V
    distances[src] = 0

    # 3. add src,0 to priority queue
    priority_queue = [(0, src)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the distance is greater than the recorded distance, skip
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path to the neighbor has been found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    V = 6
    edges = [
        (0, 1, 7),
        (0, 2, 9),
        (0, 5, 14),
        (1, 2, 10),
        (1, 3, 15),
        (2, 3, 11),
        (2, 5, 2),
        (5, 4, 9),
        (3, 4, 6)
    ]
    src = 0
    distances = dijkstra(V, edges, src)
    print("Shortest distances from source vertex", src, ":", distances)