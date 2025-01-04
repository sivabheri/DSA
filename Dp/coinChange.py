# Coin change : Unbounded KnapSack variation

''' 
# Variation 1 : Find the total No of ways that you can pay the amount with given denominations.
we are given an array of coins representing coins of different denominations , and some target.

'''

''' 
# Variation 2 : Find the minimum coins required to pay the amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

'''
#Note: There is unlimited supply of coins.

from typing import List
class Solution:
    def minCoins(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        coins = coins[::-1]
        dp = [[float('inf')]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(amount+1):
                if j%coins[0]==0:
                    dp[i][j] = j // coins[0] 
                    ''' let us say coins[] :3 and amount = 4-> so by taking any no of 3rupee coins we can't make 4 ,so ans remain float('inf')
                    	if coins : [3] and amount :60, min 3 rupee coins to make 60 are : 20 ie 60//3 
                   '''
                
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if (coins[i-1]<=j):
                    dp[i][j] = min(1+dp[i][j-coins[i-1]] , dp[i-1][j]) # here we add 1 when we pick becoz, if the coin can get amount it will be used for 1 time.
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount] if dp[n][amount]!=float('inf') else -1
    def totalways(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        coins = coins[::-1]
        dp = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(amount+1):
                if j==0:
                    dp[i][j] = 1
                if i==0:
                	dp[i][j] = 0
                   
                
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if (coins[i-1]<=j):
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j] 
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount] 
    
if __name__ == '__main__':
	
	obj = Solution()

	coins = [1,2,5,10,20,50,100,500,1000]
	amount = 123

	ans = obj.minCoins(coins,amount)
	print(f'Min no of coins needed to pay {amount} is: {ans}')
	print(f'Total no of ways to pay {amount} is: {obj.totalways(coins,amount)}')