# Leetcode - 1574
'''
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
'''
from dataclasses import dataclass
class Solution:
	# @dataclass
	def countSubarrays(self,arr:list) -> int:

		n = len(arr)
		if n<=1:
			return 0

		left,right = 0,n-1

		while left < n-1 and arr[left]<=arr[left+1]:
			left+=1

		if left==n-1:
			return 0

		while right>0 and arr[right-1]<=arr[right]:
			right-=1

		min_len = min(n-left-1,right)

		i,j = 0, right

		while i<left+1 and j<n:

			if arr[i] <= arr[j]:
				min_len = min(min_len,j-i-1)
				i+=1
			else:
				j+=1
		return min_len


if __name__ == '__main__':
	
	arr = [int(i) for i in input().strip('[]').split(',')]

	obj = Solution()

	count = obj.countSubarrays(arr)

	print(f'Minimum length of Subarray to remove is: {count}')