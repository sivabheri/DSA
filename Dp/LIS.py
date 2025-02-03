# Longest Increaing Subsequence

''' Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        # Memo + recursion 
        def LIS(ind, prev):
            # Base case: when we have considered all elements
            if ind == n:
                return 0

            if dp[ind][prev + 1] != -1:  # prev + 1 to handle -1 index
                return dp[ind][prev + 1]

            # Option 1: Do not pick the current element
            nopick = LIS(ind + 1, prev)
            
            # Option 2: Pick the current element if it's valid
            pick = 0
            if prev == -1 or nums[prev] < nums[ind]:
                pick = 1 + LIS(ind + 1, ind)

            # Store the result in the dp array
            dp[ind][prev + 1] = max(pick, nopick)
            return dp[ind][prev + 1]
        
        return LIS(0, -1)

    def method2(self,nums) : 

    	n = len(nums)

    	dp = [1]*n

    	for i in range(n):
    		for prev in range(i) :
    			if nums[i] > nums[prev] and dp[i] < dp[prev]+1:
    				dp[i] = dp[prev]+1
    	return max(dp)

if __name__ == '__main__':
	
	arr = [int(i) for i in input().strip('[]').split(',')]
	obj = Solution()
	max_len = obj.method2(arr)
	print(f"Length of LIS is : {max_len}")