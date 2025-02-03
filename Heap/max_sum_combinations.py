# Maximum Sum Combinations

''' 
we will be given two arrays and an integer k.
we need to return top k combinations of max sums.
'''
from typing import List
import heapq

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A: List[int], B: List[int], C: int) -> List[int]:
        # Sort both arrays in descending order
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        # Max-heap to store the maximum sums
        max_heap = []
        # Set to track visited combinations to avoid duplicates
        visited = set()
        
        # Push the initial combination (A[0] + B[0]) into the heap
        initial_sum = A[0] + B[0]
        max_heap.append((-initial_sum, 0, 0))  # Store as (-sum, index in A, index in B)
        visited.add((0, 0))
        
        result = []
        
        while C > 0 and max_heap:
            # Get the maximum sum combination
            current_sum, i, j = heapq.heappop(max_heap)
            result.append(-current_sum)  # Store the positive sum
            
            # Generate new combinations
            if i + 1 < len(A):  # Next element in A
                new_sum = A[i + 1] + B[j]
                if (i + 1, j) not in visited:
                    heapq.heappush(max_heap, (-(new_sum), i + 1, j))
                    visited.add((i + 1, j))
            
            if j + 1 < len(B):  # Next element in B
                new_sum = A[i] + B[j + 1]
                if (i, j + 1) not in visited:
                    heapq.heappush(max_heap, (-(new_sum), i, j + 1))
                    visited.add((i, j + 1))
            
            C -= 1  # Decrease the count of combinations to find
        
        return result

# Example usage
solution = Solution()
A = [1, 4, 2]
B = [3, 5, 1]
C = 3
print(solution.solve(A, B, C))  # Output: [9, 7, 7]