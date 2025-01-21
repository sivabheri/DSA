# Khan's Algortitm for Topological Sorting : Using BFS

''' 
As we Know that Topological sort is Linear Ordering or vetices of a Directed Acyclic Graph (DAG).

Here in this algorithm we find the topological order based on the indegree of vertices.

Algorithm:

step 1: we will take a array to store the indegrees of all the vertices
step 2: we will add those vertices to the Queue.
step 3: pefrom bfs, such that we visit the poped item's neigbours
		Now, reduce the indegree(neighbour) by one 
		if indegree(neighbour)==0: then we add it to the Queue and repeat the bfs.

** check for cycles: 
  if the len(topological orderlist) != no of vertices then: Cycle exists

Note: we add those vertices to the resultant array when their indegree is 0 based on the order of bfs. 
'''
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.indegree = defaultdict(int)
        self.vertices = set()  # To keep track of all vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v] += 1
        self.vertices.add(u)
        self.vertices.add(v)

    # Perform Topological Sort
    def topologicalsort(self):
        # Step 1: Add vertices with indegree = 0 to the queue
        queue = deque()
        for vertex in self.vertices:
            if self.indegree[vertex] == 0:
                queue.append(vertex)
        
        res_arr = []

        # Step 2: Perform BFS-like processing
        while queue:
            processed_vertex = queue.popleft()
            res_arr.append(processed_vertex)

            for neighbor in self.graph[processed_vertex]:
                self.indegree[neighbor] -= 1
                if self.indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Check for cycles
        if len(res_arr) != len(self.vertices):
            print('The Graph contains cycles and is not a DAG.')
            return []

        return res_arr

if __name__ == '__main__':
    graph = Graph()

    # Adding edges to the graph
    graph.add_edge(5, 0)
    graph.add_edge(5, 2)
    graph.add_edge(0, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(1, 4)

    print(f"The topological order of vertices is: {graph.topologicalsort()}")

