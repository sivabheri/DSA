# LEETCODE: 1639
# Hard

''' You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")'''
from typing import List
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        mod = 10**9+7

        m,n = len(words),len(words[0])

        target_len = len(target)
        memo = {}
        def dfs(tgt_idx,last_idx):
            if tgt_idx == target_len:
                return 1
            if (tgt_idx,last_idx) in memo:
            	return memo[(tgt_idx,last_idx)]

            total_ways = 0

            for j in range(m):

                for k in range(last_idx+1,n):
                    if words[j][k] == target[tgt_idx]:
                        total_ways += dfs(tgt_idx+1,k)
                        total_ways %= mod
            memo[(tgt_idx,last_idx)] = total_ways
            return memo[(tgt_idx,last_idx)]
        return dfs(0,-1)

    def dpsolution(self, words, target):

    	mod = 10**9+7

    	m , n = len(words) , len(words[0])
    	tgt_len = len(target)

    	count = [[0]*26 for _ in range(tgt_len+1)]

    	for word in words:
    		for ind,char in enumerate(word):
    			count[ind][ord(char)-ord('a')] += 1
    	
    	# DP array: dp[tgt_idx][last_idx]
    	# dp[i][j] represents the number of ways to form target[0:i] using words[0:j] 
    	dp = [[0]*(n+1) for _ in range(tgt_len+1)]
    	dp[0] = [1]*(n+1)

    	for tgt_idx in range(1,tgt_len+1):
    		for last_idx in range(n):
    			dp[tgt_idx][last_idx+1] = dp[tgt_idx][last_idx]
    			char_idx = ord(target[tgt_idx-1])-ord('a')
    			if count[last_idx][char_idx] > 0:
    				dp[tgt_idx][last_idx + 1] += dp[tgt_idx - 1][last_idx] * count[last_idx][char_idx]
    				dp[tgt_idx][last_idx + 1] %= mod
    	return dp[tgt_len][n]


if __name__ == '__main__':
	
	obj = Solution()

	words = ["acca","bbbb","caca"]
	target ="aba"

	print(f'Total no of ways to form the target string is : {obj.dpsolution(words,target)}')