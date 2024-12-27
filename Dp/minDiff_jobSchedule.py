# LEETCODE - 1335 - Hard
# asked in Amazon 2024

''' 
you are given a jobdifficulty array arr , total days of work d.
arr[i] difficulty of ith job,
to do jth job we must have done the prior job.

Conditions:
1. each day atleast 1 job must be done.
2. difficulty on ith day is maximum difficult job done on that day.
3. Find the minimum difficulty after d days, = sum of max difficulites of each day. 
'''
from typing import List
from typing import List

class Solution2:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        # Edge case: Not enough jobs for the days
        if n < d:
            return -1
        
        # Initialize dp table with infinity
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # Base case: No jobs, no days = 0 difficulty
        
        # Fill the DP table
        for days in range(1, d + 1):  # Iterate over the number of days
            for i in range(days, n + 1):  # Iterate over the number of jobs
                max_difficulty = 0
                # Try splitting jobs from k to i
                for k in range(i - 1, days - 2, -1):  # Iterate backwards for max_difficulty
                    max_difficulty = max(max_difficulty, jobDifficulty[k])
                    dp[i][days] = min(dp[i][days], dp[k][days - 1] + max_difficulty)
        
        # The result is the minimum difficulty to schedule all jobs into d days
        return dp[n][d]

class Solution1:
    def recursive_bf(self,d,ind,arr):
        n = len(arr)
        if d==0:
            return 0 if ind==n else float('inf')
        if ind>=n:
            return float('inf')
        maxD = float('-inf')
        FinalD = float('inf')
        for i in range(ind,n-d+1):

            maxD = max(maxD,arr[i])

            result_i = maxD + self.recursive_bf(d-1,i+1,arr)

            FinalD = min(FinalD,result_i)
        return FinalD         

    def memo(self,d,ind,arr,dp):
        n = len(arr)
        if d==0:
            return 0 if ind==n else float('inf')
        if ind>=n:
            return float('inf')

        if dp[ind][d] != -1:
        	return dp[ind][d]

        maxD = float('-inf')
        FinalD = float('inf')
        for i in range(ind,n-d+1):

            maxD = max(maxD,arr[i])

            result_i = maxD + self.memo(d-1,i+1,arr,dp)

            FinalD = min(FinalD,result_i)

        dp[ind][d] = FinalD
        return dp[ind][d]      
    def minDifficulty(self, arr: List[int], d: int) -> int:
        
        n = len(arr)
        if n<d:
            return -1
        dp = [[-1]*(d+1) for _ in range(n)]

        return self.memo(d,0,arr,dp)

    '''
    First Base Case: if d == 0

    What it means:
    If there are no more days left (d == 0), we need to check if we've processed the entire array.
    If ind == n (i.e., all elements in the array have been processed), return 0, because no difficulty is left to compute.
    Otherwise, if there are still elements left in the array but no days to process them, return float('inf'), because it's impossible to make a valid split.
    Example:

    Input: arr = [6, 5, 4], d = 0, ind = 3
    Since all elements have been processed (ind == n), return 0.
    Input: arr = [6, 5, 4], d = 0, ind = 1
    Since there are unprocessed elements (ind != n), return float('inf').
    Second Base Case: if ind >= n

    What it means:
    If the starting index ind has reached or exceeded the end of the array (ind >= n), but there are still days left (d > 0), return float('inf').
    This is because there are no elements left in the array to process, so it's impossible to split the array further.
    Example:

    Input: arr = [6, 5, 4], d = 1, ind = 3
    Since ind >= n and we still have 1 day left, return float('inf').
    '''
if __name__ == '__main__':
	
	obj1 = Solution1()
	obj2 = Solution2()

	arr = [int(i) for i in input().strip('[]').split(',')]

	d = int(input())

	answer = obj2.minDifficulty(arr,d)

	print(f'Minimum difficulty to finish all jobs in {d} days is : {answer}')