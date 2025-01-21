# Topological Sort - DFS

''' 
Topological sorting is a linear ordering of vertices in a DAG.
such that if there is an edge from u -> v then u comes before v in the ordering.
Usfull in scenarios like Scheduling tasks, resolving dependencies etc..


Algorithm:
	1. start with any unvisited vertex
	2. pefrorm dfs until we stop doing which means when no un visited neighbours are there.
	3. after that add the node to stack
	4. stack now has the reverse topological order

example:
consider the following graph:
    5
   / \
  0   2
   \ / \
    3   1
     \
      4

The edges of the graph can be represented as:

5 → 0
5 → 2
0 → 3
2 → 3
3 → 4
1 → 4

'''

from collections import defaultdict
class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self,u,v):
		self.graph[u].append(v)

	#main
	def topologicalsort(self):

		visited = set()
		stack = [] # to store topological order of vertices

		# step 2
		def dfs(start):
			#1. Mark it as visited
			visited.add(start)
			
			#2. perform dfs on its unvisited neighbours
			for neighbor in self.graph[start]:
				if neighbor not in visited:
					dfs(neighbor)

			#3. if dfs(node) is done then add it to stack
			stack.append(start)

		# step 1
		for i in list(self.graph):
			if i not in visited:
				dfs(i)

		#step 3
		return stack[::-1]


if __name__ == '__main__':
	
	graph = Graph()

	graph.add_edge(5,0)
	graph.add_edge(5,2)
	graph.add_edge(0,3)
	graph.add_edge(2,3)
	graph.add_edge(3,4)
	graph.add_edge(1,4)

	print(f"The topological order of vertices is : {graph.topologicalsort()}")
	