# 0/1 Knapsack problem

class Solution:

    # Function to return max value that can be put in knapsack of capacity.
    def recursion(self,wt,val,W,n,dp):
        # base case
        if (n == 0 or W == 0):
            return 0
        # memoized val ?
        if (dp[n][W] != -1):
        	return dp[n][W]
        # recusive call
        if (wt[n-1]<=W):
            dp[n][W] = max(val[n-1]+self.recursion(wt,val,W-wt[n-1],n-1,dp),self.recursion(wt,val,W,n-1,dp))
        else:
        	dp[n][W] =  self.recursion(wt,val,W,n-1,dp)
        
        return dp[n][W]
    def knapSack(self, capacity, val, wt):
        # code here
        n = len(wt)
        # recursive solution
        # return self.recursion(wt,val,capacity,n)

        # memoization
        # dp = [[-1]*(capacity+1) for _ in range(n+1)]
        # return self.recursion(wt,val,capacity,n,dp)

        # tabulation
        dp = [[0]*(capacity+1) for _ in range(n+1)]

        for i in range(n+1):
        	for j in range(capacity+1):
        		if i==0 or j==0:
        			dp[i][j] = 0

        for i in range(1,n+1):
        	for j in range(1,capacity+1):
        		if wt[i-1]<=j:
        			dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
        		else:
        			dp[i][j] = dp[i-1][j]
        return dp[n][capacity]
        
        
if __name__ == '__main__':
	
	wt = [int(i) for i in input().split()] # 1 2 3
	val = [int(i) for i in input().split()] # 4 5 1
	capacity = int(input()) # 4

	obj = Solution()

	print(f'Max Profit can be obtained: {obj.knapSack(capacity,val,wt)}')