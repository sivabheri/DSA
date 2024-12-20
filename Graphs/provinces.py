# LEET CODE - 547

''' 
We are given a adjacency matrix, we have to find the total no of provinces.
A fully connected graph is called a province.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
'''

class Solution:


	def calProvinces(self,adj):

		def dfs(city) : 
			
			for neighbor in range(n):

				if adj[i] == 1 and visited[neighbor] == False:
					visited[neighbor] = True
					dfs(neighbor)
		n = len(adj)
		provinces = 0

		visited = [False]*n

		for i in range(n):

			# we say there is a province when after performing dfs or bfs traversal we still have a unvisited node
			if visited[i] == False:

				provinces += 1
				visited[i] = True
				dfs(i)

		return provinces

if __name__ == '__main__':
	
	obj = Solution()

	adj = [[1,0,0],[0,1,0],[0,0,1]]

	res = obj.calProvinces(adj)

	print(res)