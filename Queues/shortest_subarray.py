# Leetcode-862 : Shortest subarray with sum equal to K
'''Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
'''
from collections import deque
class Solution:
    
    def shortestSubarray(self, nums, k) :
        
        n = len(nums)
        prefix = [0]*(n+1)
        
        for i in range(n):
            prefix[i+1] = prefix[i]+nums[i]

        dq = deque()
        mlen = float('inf')
        for i in range(n+1):

            while dq and prefix[i] - prefix[dq[0]] >= k:
                mlen = min(mlen,i - dq.popleft())
            # while dq and prefix[i] <= prefix[dq[-1]]:
                # dq.pop()
            dq.append(i)

        return mlen if mlen!=float('inf') else -1

if __name__ == '__main__':
	
	obj = Solution()

	arr = [int(i) for i in input().strip('[]').split(',')]
	k = int(input())
	ans = obj.shortestSubarray(arr,k)
	print(f'The length of subarry with sum==k is {ans}')