# Number of Enclave - Leetcode 1020

''' You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.


Intution : 
start with all the boundary cell having 1 ,
perform dfs on them like if any neigbouring cells also 1 then make them 0 including the boundary cell.

after performing dfs all the cells connecting the sea shore will become 0.
so if there are any cells in the gird with 1 then they are un reachable we can return their count.
'''
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        from collections import deque
        row,col = len(grid),len(grid[0])
        dirns = [(0,1),(0,-1),(1,0),(-1,0)]

        # dfs
        def dfs(r,c):

            # mark 1 as 0
            grid[r][c] = 0
            for dr,dc in dirns:
                newr = r+dr
                newc = c+dc
                if 0<=newr<row and 0<=newc<col and grid[newr][newc]==1:
                    dfs(newr,newc)

        # main
        for i in range(row):
            for j in range(col):
                if (i==0 or i==row-1 or j==0 or j==col-1) and grid[i][j]==1:
                    dfs(i,j) # we mark 0 for all those points that reach the shore
        
        # after converting the matrix if still there are 1s then count them as they never reach the shore
        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    cnt+=1
        return cnt

if __name__ == '__main__':
	
	obj = Solution()
	grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
	print(f'No of non reachable enclaves are : {obj.numEnclaves(grid)}')