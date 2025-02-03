# Sum of Subarray Ranges

''' 
You are given an integer array nums. 
The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
Return the sum of all subarray ranges of nums.


Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Example 2:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.'''

from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        n = len(nums)

        nextsmaller = [n] * n
        nextgreater = [n] * n

        prevsmaller = [-1] * n
        prevgreater = [-1] * n

        stack = []

        # find next smaller and next greater
        # next smaller which mean for how many elements does nextsmaller[i] is smaller
        # next greater which mean for how many elements does nextgreater[i] is greater
        # lly do for prev 

        # min contribution = nextsmaller - i   *  i - prevsmaller
        # max contribution = nextgreater - i   *  i - prevgreater
        # total contribution = max - min

        # smaller
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                nextsmaller[stack.pop()] = i
            stack.append(i)
        
        stack.clear()

        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                prevsmaller[stack.pop()] = i
            stack.append(i)
        
        stack.clear()
        total = 0

        # greater
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                nextgreater[stack.pop()] = i
            stack.append(i)
        
        stack.clear()

        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                prevgreater[stack.pop()] = i
            stack.append(i)
        
        stack.clear()

        maxc, minc = 0, 0
        for i in range(n):
            maxc += nums[i] * (nextgreater[i] - i) * (i - prevgreater[i]) 
        for i in range(n):
            minc += nums[i] * (nextsmaller[i] - i) * (i - prevsmaller[i]) 
        
        return maxc - minc
if __name__ == '__main__':
	
	arr = [1,2,3]
	obj = Solution()
	ans = obj.subArrayRanges(arr)
	print(f'Sum of subArrayRanges is : {ans}')