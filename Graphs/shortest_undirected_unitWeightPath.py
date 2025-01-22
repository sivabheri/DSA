# Shortes Path in an Undirected graph of unit weight

'''  BFS for Shortest Path
	step 1: Graph Representation: Use an adjacency list to represent the graph.
	step 2: Initialize BFS: Use a queue to keep track of nodes to explore
		and a list to store the shortest distance from the source node to each node.
	step 3: Process Nodes: For each node, explore its neighbors. 
		If a neighbor has not been visited, update its distance and add it to the queue.
	step 4:Return the Result: After processing all nodes, return the list of shortest distances.'''

from collections import deque
from typing import List, Tuple

def shortest_path(graph: List[List[int]], start: int) -> List[int]:
    n = len(graph)
    distances = [-1] * n  # Initialize distances with -1 (unreachable)
    distances[start] = 0  # Distance to the start node is 0

    queue = deque([start])  # Initialize the queue with the start node

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # If the neighbor hasn't been visited
                distances[neighbor] = distances[current] + 1  # Update distance
                queue.append(neighbor)  # Add neighbor to the queue

    return distances

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = [
        [1, 2],    # Node 0 is connected to Node 1 and Node 2
        [0, 3, 4], # Node 1 is connected to Node 0, Node 3, and Node 4
        [0, 4],    # Node 2 is connected to Node 0 and Node 4
        [1],       # Node 3 is connected to Node 1
        [1, 2]     # Node 4 is connected to Node 1 and Node 2
    ]
    
    start_node = 0
    distances = shortest_path(graph, start_node)
    print("Shortest distances from node", start_node, ":", distances)