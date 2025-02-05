# Max Consecutice Ones : LEETCODE - 1004

''' 
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10

Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

from collections import deque
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left,right = 0,0
        mcnt = 0
        # we use deque only to store the every occurence of zero not other numbers
        # if asked about unique numbers we use dictionary to store last occence for every number 
        dq = deque()
        cnt = 0
        mlen = 0

        # case 1 :  when no flips
        if k==0:
            cur = 0
            for num in nums:
                if num==1:
                    cur+=1
                else:
                    cur=0
                mlen = max(mlen,cur)
            return mlen

        # case 2: k>0 we can do atmost k flips so we use cnt to keep track of no of 0s
        for right in range(len(nums)):

            if nums[right] == 0:
                cnt+=1
                if cnt>k: # we move left after the first occurece of zero for that window
                    lastzero = dq.popleft()
                    left = lastzero + 1
                    cnt-=1
                dq.append(right) # stores all occences of zeros until cnt>k if cnt>k we pop the first occuence and move our left to there.
            mlen = max(mlen,right-left+1)
        return mlen
if __name__ == '__main__':
	obj = Solution()
	arr = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
	k = 3
	ans = obj.longestOnes(arr,k)
	print(f'Max Consecutive one after {k}flips are : {ans} ')