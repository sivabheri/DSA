# Shorted Path in DAG

''' 
Finding the list of shortest distances from the start node to all other nodes.
'''

from collections import defaultdict, deque
from typing import List, Tuple

def topological_sort(graph: List[List[int]], n: int) -> List[int]:
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return topo_order

def shortest_path_dag(graph: List[List[int]], weights: List[List[int]], start: int) -> List[float]:
    n = len(graph)
    topo_order = topological_sort(graph, n)
    
    distances = [float('inf')] * n
    distances[start] = 0

    for u in topo_order:
        if distances[u] != float('inf'):
        	# from u to all the other nodes we update the distance[v] only if the updated distance < old distance[v]
            for idx, v in enumerate(graph[u]):
                if distances[u] + weights[u][idx] < distances[v]:
                    distances[v] = distances[u] + weights[u][idx]

    return distances

# Example usage
if __name__ == "__main__":
    graph = [
        [1, 2],    # Node 0 is connected to Node 1 and Node 2
        [3],       # Node 1 is connected to Node 3
        [3],       # Node 2 is connected to Node 3
        []         # Node 3 is a terminal node
    ]
    
    weights = [
        [1, 4],    # Weights for edges from Node 0 to Node 1 and Node 2
        [2],       # Weight for edge from Node 1 to Node 3
        [1],       # Weight for edge from Node 2 to Node 3
        []         # No outgoing edges from Node 3
    ]
    
    start_node = 0
    distances = shortest_path_dag(graph, weights, start_node)
    print("Shortest distances from node", start_node, ":", distances)