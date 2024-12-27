# LEETCODE - 494

''' 
we will be given an array of intergers and a target value.

for each element of the array we can assign either + or - signs,
such that the sum of that array might equals to the target.

so, we need to find the total no of ways or combinations of the array that gives the sum equals to the target.

Example 1: 
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input: nums = [1], target = 1
Output: 1
'''
from typing import List
class Solution:

	# Bruteforce: Using Recursion
    def method1(self, nums: List[int], target: int) -> int:
        
        def backtrack(index,cur_sum):

            if index==len(nums):
                return 1 if cur_sum == target else 0
            
            plus = backtrack(index+1,cur_sum+nums[index])
            minus = backtrack(index+1,cur_sum-nums[index])
            
            return plus + minus
        
        return backtrack(0,0)
        # we will get TLE

    # optimal : Dp
    def method2(self, nums: List[int], target: int) -> int:
        

       	total_sum = sum(nums)
       	if (total_sum+target) %2 !=0 or (total_sum+target) < 0:
       		return 0

       	sumA = (total_sum+target) //2

       	dp = [0] * (sumA+1)

       	dp[0] = 1

       	for num in nums:
       		# here dp[i] = values that we can get from num to SumA when we do different operations on array
       		for i in range(sumA,num-1,-1):
       			# If we want to form the sum j, and we decide to include num, then the remaining sum we need to form is j - num.
       			dp[i] += dp[i-num]

       	return dp[sumA]

       	'''
		The task is to find the number of ways to assign + or - signs to the elements of an array.
		so that their sum equals a given target. This can be visualized as partitioning the array into two groups:

		Group A: Numbers with a + sign.
		Group B: Numbers with a - sign.
		The relationship between these groups can be derived as:

		sumA − sumB	=	target  -- eqn(1)
		sumA + sumB =   total_arr_sum  -- eqn(2)

		so, we just need to find no of ways we get sumA.
		That can be possible only when , target + total_arr_sum % 2 == 0 and target + total_arr_sum >= 0 ie. from the two eqns.

		To find no of ways to get sumA, sumA = target + total_arr_sum // 2 from the two eqns

		we take dp array of size = sumA+1

		base conditon : dp[0] = 1 # we we select no elements

		#for each num  we may form sumA
		for num in nums:

			for i in range(SumA, num-1, -1) :

				dp[i] += dp[i-num] 

		example: 
		Input:
		nums = [1, 2, 1], target = 3
		Derived 
		sumA = 4
		sumA = 4.

		Iteration:
		Initial dp = [1, 0, 0, 0, 0] (only one way to make sum 0: select no elements).
		First Number: num = 1

		For j = 4 to 1:
		j = 1: 
		dp[1] += dp[1 - 1]
		dp[1] += dp[0]
		dp[1] = 0 + 1 = 1
		Updated dp = [1, 1, 0, 0, 0].

		Second Number: num = 2

		For j = 4 to 2:
		j = 2: 
		dp[2] += dp[2 - 2]
		dp[2] += dp[0]
		dp[2] = 0 + 1 = 1

		j = 3: 
		dp[3] += dp[3 - 2]
		dp[3] += dp[1]
		dp[3] = 0 + 1 = 1
		Updated dp = [1, 1, 1, 1, 0].

		Third Number: num = 1

		For j = 4 to 1:
		j = 4: 
		dp[4] += dp[4 - 1]
		dp[4] += dp[3]
		dp[4] = 0 + 1 = 1

		j = 3: 
		dp[3] += dp[3 - 1]
		dp[3] += dp[2]
		dp[3] = 1 + 1 = 2
		Updated dp = [1, 2, 1, 2, 1].

		Final dp:
		dp = [1, 2, 1, 2, 1]
		The number of ways to form sumA = 4 is dp[4] = 1.
    	'''
    	

if __name__ == '__main__':
	
	obj = Solution()

	arr = [1,1,1,1,1]

	target = 3

	ways = obj.method2(arr,target)

	print(f'The total no of ways to get the target {target} is : {ways}')