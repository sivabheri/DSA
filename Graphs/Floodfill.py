# Flood Fill - BFS : Leetcode - 733

'''
You are given an image represented by an m x n grid of integers image,
where image[i][j] represents the pixel value of the image. 
You are also given three integers sr, sc, and color. 
Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

-Begin with the starting pixel and change its color to color.
-Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel,
 either horizontally or vertically) and shares the same color as the starting pixel.
-Keep repeating this process by checking neighboring pixels of the updated pixels
 and modifying their color if it matches the original color of the starting pixel.
-The process stops when there are no more adjacent pixels of the original color to update.
-Return the modified image after performing the flood fill.

Note : carefully observe the initial queue insertion.
if we insert only one item in the queue then the behavior or While loop changes.
compare it with Rotten Oranges problem. 

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]
'''
from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the original color of the starting pixel
        original_color = image[sr][sc]
        
        # If the original color is the same as the new color, no need to proceed
        if original_color == color:
            return image
        
        row, col = len(image), len(image[0])
        queue = deque([(sr, sc)])  # Initialize the queue with the starting pixel
        dirns = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Directions for right, left, up, down
        
        # Perform BFS
        while queue:
            r, c = queue.popleft()
            image[r][c] = color  # Change the color of the current pixel
            
            for dr, dc in dirns:
                newr, newc = r + dr, c + dc
                # Check if the new position is within bounds and has the original color
                if 0 <= newr < row and 0 <= newc < col and image[newr][newc] == original_color:
                    queue.append((newr, newc))  # Add the neighboring pixel to the queue
        
        return image

if __name__ == "__main__":
    # Example usage
    sol = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr, sc, color = 1, 1, 2
    result = sol.floodFill(image, sr, sc, color)
    print("Modified Image:")
    for row in result:
        print(row)
