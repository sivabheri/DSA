# Rotten Oranges - Leetcode-994
''' 
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''
from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        freshcnt = 0
        queue = deque()
        row, col = len(grid), len(grid[0])
        
        # Step 1: Initialize the queue with all rotten oranges and count fresh oranges
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))  # Add rotten orange to the queue
                if grid[i][j] == 1:
                    freshcnt += 1  # Count fresh oranges
        
        # Directions for right, left, down, up
        dirns = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0
        
        # Step 2: Perform BFS to rot the oranges
        while queue and freshcnt > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in dirns:
                    newr, newc = r + dr, c + dc
                    # Check if the new position is within bounds and is a fresh orange
                    if 0 <= newr < row and 0 <= newc < col and grid[newr][newc] == 1:
                        freshcnt -= 1  # Decrease the count of fresh oranges
                        grid[newr][newc] = 2  # Rot the fresh orange
                        queue.append((newr, newc))  # Add the newly rotten orange to the queue
            
            minutes += 1  # Increment minutes after processing this level
        
        # Step 3: Check if there are any fresh oranges left
        return minutes if freshcnt == 0 else -1

if __name__ == "__main__":
    # Example usage
    sol = Solution()
    
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    result = sol.orangesRotting(grid)
    print(f"Output: {result}")  # Output: 4
    
