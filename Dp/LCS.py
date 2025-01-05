# Longest Common Subsequence

'''Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0. '''

''' 
choice diagram:

						fun(n,m)
						/		\
			if x[n]==y[m]		else:
			|					/	\
		fun(n-1,m-1)	fun(n-1,m)	fun(n,m-1)
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # memoization with recursion
        n = len(text1)
        m = len(text2)
        
        # dp = [[-1]*(m+1) for _ in range(n+1)]
        def recursion(x,y,n,m):
            
            # base condition
            if n==0 or m==0:
                return 0
            
            # check if it is already solved
            if dp[n][m]!=-1:
            	return dp[n][m]

            # choice diagram
            if x[n-1]==y[m-1]:
                dp[n][m] =  1 + recursion(x,y,n-1,m-1)
            else:
                dp[n][m] =  max( recursion(x,y,n-1,m) , recursion(x,y,n,m-1))

            return dp[n][m]
        # return recursion(text1,text2,len(text1),len(text2))

        # Top-down
        dp = [[0]*(m+1) for _ in range(n+1)]

        # base conditon : when either of the strings are empty then no lcs
        for i in range(n+1):
        	for j in range(m+1):
        		if i==0 or j==0:
        			dp[i][j]=0
       	# choice diagram
        for i in range(1,n+1):
        	for j in range(1,m+1):
        		if text1[i-1]==text2[j-1]:
        			dp[i][j] = 1 + dp[i-1][j-1]
        		else:
        			dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]

if __name__ == '__main__':
	
	obj = Solution()
	text1 = input()
	text2 = input()
	
	ans = obj.longestCommonSubsequence(text1,text2)
	print(f"The Length longest Common Subsequence in both the strings is: {ans}")