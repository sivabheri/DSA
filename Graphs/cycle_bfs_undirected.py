# Cycle Detection in Undirected Graph - BFS

''' 
Initialization: Create a queue to perform BFS and a set to keep track of visited nodes.

BFS Traversal:

	- For each unvisited node, start a BFS traversal.
	- For each node, mark it as visited and enqueue its neighbors.
	- If a neighbor has already been visited and is not the parent of the current node, a cycle is detected.
	- Repeat: Continue this process until all nodes have been processed.

let say  0
		/ \
	   1 - 2

if (neighbour is visited and  neighbor != parent )is crucial because:

If we encounter a neighbor that is the same as the parent, it means we are simply traversing back to the node we just came from, which is not a cycle.
If the neighbor is different from the parent and has already been visited, it indicates that there is a back edge, which forms a cycle.

see here 1 and 2 has a common parent 0:
but when we doing bfs if neighbour(1 ie = 2)!==parent(0):
	which means there is an edge between 1 and 2 so, if form a cycle.

'''
from collections import defaultdict,deque
class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def edge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def cycledetection(self):

		visited = set()
		def bfs(start):

			queue = deque([(start,-1)])
			visited.add(start)

			while queue:
				node,parent = queue.popleft()

				for neighbor in self.graph[node]:
					if neighbor not in visited:
						visited.add(neighbor)
						queue.append((neighbor,node))

					elif neighbor!=parent:
						return True # Cycle exists
			return False

		# in undirected graph there can many disconnected components 
		# we have to check cycle in all the components
		for node in self.graph:
			if node not in visited:
				if bfs(node):
					return True
		return False

if __name__ == '__main__':
	
	g = Graph()
	g.edge(0,1)
	g.edge(1,2)
	g.edge(0,2)

	print(f'Is cylce detected ? {g.cycledetection()}')