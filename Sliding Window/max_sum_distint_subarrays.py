# LeetCode: 2461 - Maximum Sum of Distinct Subarrays Length K

'''
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.'''
class Solution:
    def maximumSubarraySum(self, nums, k):
        from collections import defaultdict
        n = len(nums)
        imax = -1*2**31-1
        msum = -1*2**31-1
        csum = 0
        left,right = 0,0 # left is used to maintain the window having k elements, right to iterate the array
        freq = defaultdict(int)
        while (right < n):
            
            #1st. add the elements to seen if not in seen or initial conditions
            freq[nums[right]]+=1
            csum+=nums[right]

            if right-left+1 > k:
                csum-=nums[left]
                freq[nums[left]]-=1
                if freq[nums[left]] ==0:
                    del freq[nums[left]]
                left+=1
            
            if right-left+1==k and len(freq)==k:
                msum = max(msum,csum)
            right+=1
        return msum if msum!=imax else 0

if __name__ == '__main__':
    
    obj = Solution()
    arr = [int(i) for i in input("input: ").strip('[]').split(',')]
    k = int(input('k: '))
    print('Output: ',obj.maximumSubarraySum(arr,k))