#Rod Cutting - Unbounded KnapSack variation

'''
Given a rod of length n(size of price) inches and an array of prices, price. 
price[i] denotes the value of a piece of length i. 
Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Example:
Input: price[] = [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
Explanation: The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5+17=22.

Input: price[] = [3, 5, 8, 9, 10, 17, 17, 20]
Output: 24
Explanation: The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1]= 8*3 = 24.

Input: price[] = [1, 10, 3, 1, 3, 1, 5, 9]
Output: 40 '''
class Solution:
    def cutRod(self, price):
        
        # Same code as Unbounded KnapSack
        n = len(price) # rod length
        length = [(i+1) for i in range(n)]
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        # Wt = length, capacity = n , val = price
        for i in range(n+1): # no of unique lengths
            for j in range(n+1): # capacity
                if i==0 or j==0:
                    dp[i][j] = 0
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                
                if i<=j: # length[i-1] <-> i
                    dp[i][j] = max(price[i-1] + dp[i][j-i],dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][n]
    
    def cutRod2(self,price):
        
        n = len(price)
        dp = [0]*(n+1) # for prices
        
        for i in range(1,n+1):
            for j in range(i,n+1):
                dp[j] = max(dp[j],price[i-1]+dp[j-i])
        
        return dp[n]
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = 1

    while (T > 0):
        # n = int(input())
        a = [1, 5, 8, 9, 10, 17, 17, 20]
        ob = Solution()
        print(f"Max Profit obtained: {ob.cutRod(a)}")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends