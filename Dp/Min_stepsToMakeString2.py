# Min no of Instertions and Deletions to convert String A to B

# LCS variation

''' 
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
'''
from typing import List
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # To covert string A -> B, (Directly not possible)
        # both of them Should be related to LCS
        # what is common in both of them? - LCS
        # so, To make A to LCS - we have to delete some characters
        # no of deletions = len(A) - len(LCS)
        # similarly, no of insertions = len(B) - len(LCS)

        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        #base
        # for i in range(n+1):
        #     for j in range(m+1):
        #         if i==0 or j==0:
        #             dp[i][j]=0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        clen = dp[n][m]
        insertions = n - clen
        deletions = m - clen
        total = insertions + deletions
        return total
if __name__ == '__main__':
	
	obj = Solution()
	A = input()
	B = input()
	min_steps = obj.minDistance(A,B)
	print(f'Min no of conversions to make A to B : {min_steps}')