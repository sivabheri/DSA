# Valid Path : Leetcode-1971

'''
we will be given n nodes and edge list and two nodes start and destination.
we have to return True if there is a path from start to destination else False.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
'''
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        if not edges:
            return True
        # in any graph , a valid path will definitly exists between any two node

        # if no path exists the that destination node does not lie in the source node graph

        # so if we perform dfs or bfs on source node and if we reach destn we return true else False

        # step1 : create a graph to store the edges
        from collections import defaultdict,deque
        graph = defaultdict(list)

        for edge in edges:
            u,v = edge
            graph[u].append(v)
            graph[v].append(u)
        
        #step2 : dfs or bfs on source node
        def dfs(src,dest):
            q = deque([src])
            vis = set()
            vis.add(src)
            while q:
                node = q.pop()
                for neighbour in graph[node]:
                    if neighbour == dest:
                        return True
                    if neighbour not in vis:
                        vis.add(neighbour)
                        q.append(neighbour)
            return False
        return dfs(source,destination)

if __name__ == '__main__':
	
	obj = Solution()

	n = 3
	edges = [[0,1],[1,2],[2,0]]
	source = 0
	destination = 2

	print(f'Path Exist ? : {obj.validPath(n,edges,source,destination)}')