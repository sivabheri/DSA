# Count Nice Subarrays - Leetcode: 1248

'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.


Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
'''

from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        start = 0
        ans = 0
        cnt = 0
        # consider k as no of odd : we will do k -- , cnt++ only when k==0 
        for end in range(n):
            if nums[end]%2==1:
                k-=1
                cnt = 0 # incremet count only when no of odd == k or k==0
            while k==0:
                cnt += 1
                if nums[start]%2==1:
                    k += 1 # increment k because we leaving left index having odd element
                start+=1
            ans+=cnt
        return ans 

if __name__ == '__main__':
	
	obj = Solution()
	arr = [1,1,2,1,1]
	k = 3
	ans = obj.numberOfSubarrays(arr,k)
	print(ans)

