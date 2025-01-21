# Distinct Islands

''' 
we are given a grid containg 1 as land and 0 as water.
we need count the number of islands in that grid.

Note: Island : a cell with value 1 is called an island only if it is souronded with water 0 on all its 8 sides including diagonally.
'''

from collections import deque
from typing import List

class Solution:
    def bfs(self, row: int, col: int, vis: List[List[int]], grid: List[List[str]]):
        vis[row][col] = 1
        queue = deque([(row, col)])
        n = len(grid)
        m = len(grid[0])
        
        # Directions for moving in all 8 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nrow, ncol = r + dr, c + dc
                # Check if the neighbor is valid and is an unvisited land cell
                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1 and not vis[nrow][ncol]:
                    vis[nrow][ncol] = 1
                    queue.append((nrow, ncol))  

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0]) 
        vis = [[0] * m for _ in range(n)]  # Create a visited array
        cnt = 0  # Count of islands
        
        for row in range(n):
            for col in range(m):
                # If the cell is land and not visited
                if not vis[row][col] and grid[row][col] == 1:
                    cnt += 1  
                    self.bfs(row, col, vis, grid)  # Perform BFS to mark the entire island

                # NOTE: If it is vistied and val==1: then it is land but not island
        
        return cnt

if __name__ == '__main__':
	
	obj = Solution()
	grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
	islands = obj.numIslands(grid)
	print(f"No of islands: {islands}")