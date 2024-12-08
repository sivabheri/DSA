# Leetcode - 239 : Slidinng Window Maximum

# Easy problem, just focus on Deque !

''' You are given an array of integers nums, 
	there is a sliding window of size k which is moving from the very left of the array to the very right.
 	You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window. '''
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       
        n = len(nums)
        res = []
        dq = deque() # deque used here will store the indeces of arr and can store max of K indices
        for i in range(n):

            # if window size exceeds we remove the leftmost index from the deque
            if dq and  dq[0] < i-k+1:
                dq.popleft()
            # whenever the current element of arr is greater than the last element nums[dq[-1]],
            # we dont need to store dq[-1] since it is will never going to be the maximum from the current iteration i 
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # if we hit the size of the window, we add the element at the front of dequeue index to resultant array
            if i >= k-1:
                res.append(nums[dq[0]])
        
        return res

def max_of_subarrays(k, arr):
        n = len(arr)
        q = deque()
        res = []

        for i in range(k):
        
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
        
        
        for i in range(k, n):
        
            res.append(arr[q[0]])
            while q and q[0] <= i - k:
                q.popleft()

            
            while q and arr[i] >= arr[q[-1]]:
                q.pop()

            
            q.append(i)
        
        
        res.append(arr[q[0]])

        return res
# Example usage
arr = [10, 5, 2, 7, 8, 7]
k = 3
print("Max elements in subarrays of size k:", max_of_subarrays(k,arr))


''' Explaination:
Input:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
Step-by-Step Execution:
Initialization:

result = [] (to store the maximums)
dq = deque() (to store indices of elements in nums)
Iterate through nums:

Index 0 (i = 0, value = 1):
dq is empty, so we add index 0: dq = [0]
Index 1 (i = 1, value = 3):
Remove index 0 from dq because nums[0] < nums[1] (1 < 3).
Add index 1: dq = [1]
Index 2 (i = 2, value = -1):
Add index 2: dq = [1, 2]
Now we have a complete window (indices 0 to 2), so we add the max (which is nums[dq[0]] = nums[1] = 3) to result: result = [3]
Index 3 (i = 3, value = -3):
Remove index 1 from dq because it is out of the current window (index 0 to 2).
Add index 3: dq = [2, 3]
The max for the current window (indices 1 to 3) is nums[dq[0]] = nums[1] = 3: result = [3, 3]
Index 4 (i = 4, value = 5):
Remove index 2 from dq because nums[2] < nums[4] (-1 < 5).
Remove index 3 from dq because nums[3] < nums[4] (-3 < 5).
Add index 4: dq = [4]
The max for the current window (indices 2 to 4) is nums[dq[0]] = nums[4] = 5: result = [3, 3, 5]
Index 5 (i = 5, value = 3):
Add index 5: dq = [4, 5]
The max for the current window (indices 3 to 5) is nums[dq[0]] = nums[4] = 5: result = [3, 3, 5, 5]
Index 6 (i = 6, value = 6):
Remove index 5 from dq because nums[5] < nums[6] (3 < 6).
Remove index 4 from dq because nums[4] < nums[6] (5 < 6).
Add index 6: dq = [6]
The max for the current window (indices 4 to 6) is nums[dq[0]] = nums[6] = 6: result = [3, 3, 5, 5, 6]
Index 7 (i = 7, value = 7):
Remove index 6 from dq because nums[6] < nums[7] (6 < 7).
Add index 7: dq = [7]
The max for the current window (indices 5 to 7) is nums[dq[0]] = nums[7] = 7: result = [3, 3, 5, 5, 6, 7]'''