# Cycle Detection in Undirected graph - DFS

''' 
The key idea is similar to the BFS approach: while traversing the graph, we keep track of the parent of each node. 
If we encounter a node that has already been visited and is not the parent of the current node, then a cycle exists.

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
		def dfs(start,parent):

			visited.add(start)

			for neighbor in self.graph[start]:
				if neighbor not in visited:
					dfs(neighbor,start)
				elif neighbor!=parent:
					return True
			return False
		# in undirected graph there can many disconnected components 
		# we have to check cycle in all the components
		for node in self.graph:
			if node not in visited:
				if dfs(node,-1):
					return True
		return False

if __name__ == '__main__':
	
	g = Graph()
	g.edge(0,1)
	g.edge(1,2)
	g.edge(0,2)

	print(f'Is cylce detected ? {g.cycledetection()}')