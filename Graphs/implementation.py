	class Graph:
	''' Undirected Graphs using adjacency Lists'''
	def __init__(self):
		self.graph = {}

	def add_edge(self,u,v):

		if u not in self.graph:
			self.graph[u] = []

		if v not in self.graph:
			self.graph[v] = []

		self.graph[u].append(v)
		self.graph[v].append(u)

	def remove_edge(self,u,v):

		if u in self.graph and v in self.graph[u]:
			self.graph[u].remove(v)

		if v in self.graph and u in self.graph[v]:
			self.graph[v].remove(u)

	def display(self):

		for node in self.graph:

			print(f"{node}: {self.graph[node]}")

	def bfs(self,start):

		visited = set()
		queue = [start]
		visited.add(start)
		bfs_list = []
		while queue:

			node = queue.pop(0)

			bfs_list.append(node)

			for neighbor in self.graph.get(node, []):

				if neighbor not in visited:
					visited.add(neighbor)
					queue.append(neighbor)
		return bfs_list

	def dfs_recursive(self,start,visited=None):

		if visited is None:
			visited = set()

		visited.add(start)
		print(start,end =" ")

		for neighbor in self.graph.get(start,[]):

			if neighbor not in visited:
				self.dfs_recursive(neighbor,visited)

	def dfs_iterative(self,start):

		visited = set()
		stack = [start]
		dfs_list = []
		while stack:
			node = stack.pop()
			if node not in visited:
				dfs_list.append(node)
				visited.add(node)

				for neighbor in reversed(self.graph.get(node,[])):
					if neighbor not in visited:
						stack.append(neighbor)
		return dfs_list
		''' The neighbors are added in reverse order to ensure 
		that they are processed in the correct order
		(since stacks are LIFO - Last In, First Out).'''

if __name__ == '__main__':
	
	g = Graph()

	g.add_edge(1,2)
	g.add_edge(1,3)
	g.add_edge(3,2)
	g.add_edge(2,4)
	g.add_edge(1,4)
	g.add_edge(3,4)
	g.add_edge(2,5)
	g.add_edge(4,5)

	g.display()
	
	print("DFS TRAVERSAL:",g.dfs_iterative(5))

	print("BFS TRAVERSAL:",g.bfs(5))
	

	
	