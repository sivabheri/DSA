# Count the no of subsets with the Given sum
# same as Subset Sum - (0/1 knapSack Variation)

''' You are given an array 'arr' of size 'n' containing positive integers and a target sum 'k'.
Find the number of ways of selecting the elements from the array such that the sum of chosen elements is equal to the target 'k'.
Since the number of ways can be very large, print it modulo 10 ^ 9 + 7.

Example:
Input: 'arr' = [1, 1, 4, 5]

Output: 3

Explanation: The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.'''

from typing import List

def findWays(arr: List[int], k: int) -> int:
    
    # Tabulation
    mod = 10**9+7
    # similar to SubsetSum (0/1-KnapSack Variation)

    n = len(arr)

    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(k+1):
            # we cannot make a subset with no elements to get sum>0
            if i==0:
                dp[i][j] = 0
            # we can always make a subset to get sum == 0 (empty subset)
            if j==0:
                dp[i][j] = 1
    # only difference with subset sum is:
    # There if element <= target : we can/ cannot get the target if we pick/not pick the element
    # i.e, pick || not pick
    # Here., we can/ cannot get target if we pick/not pick the element
    # if we get the target we return 1
    # pick(may get target) + not pick(may get target)
    for i in range(1,n+1):
        for j in range(1,k+1):
            
            if (arr[i-1]<=j):
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

            dp[i][j]%=mod
    return dp[n][k] 

if __name__ == '__main__':
	
	arr = [int(i) for i in input().split()]
	target = int(input())

	print(f'No of subsets that give the sum {target} are : {findWays(arr,target)}')