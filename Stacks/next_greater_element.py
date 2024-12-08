# LEETCODE - 496

class Solution:

	def nextGreaterElement(self,arr):

		stk = []
		n = len(arr)
		res = [-1]*n
		for i in range(n-1,-1,-1):
			
			while stk and arr[i]>=stk[-1]:
				stk.pop()
			
			if stk:
				res[i] = stk[-1]
			stk.append(arr[i])

		return res

if __name__ == '__main__':
	
	arr = [1,4,3,6,2,5,1]
	obj = Solution()
	print(obj.nextGreaterElement(arr))