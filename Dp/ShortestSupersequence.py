# Shortest Common Super Sequence - LCS varition

''' finding the length of common subsequence + printing '''

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        n = len(str1)
        m = len(str2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        # for i in range(n+1):
        #     for j in range(m+1):
        #         if i==0 or j==0:
        #             dp[i][j] = 0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        # len of SCS
        clen = dp[n][m]
        Lscs = n+m-clen

        ans = ''
        i,j = n,m
        while(i>0 and j>0):

            if str1[i-1] == str2[j-1]:
                ans+=str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j] > dp[i][j-1]:
                ans+= str1[i-1]
                i-=1
            else:
                ans+= str2[j-1]
                j-=1
        # if there are any characters left in str1 or str2
        while(i>0):
            ans+=str1[i-1]
            i-=1
        while(j>0):
            ans+=str2[j-1]
            j-=1
        
        return ans[::-1]

if __name__ == '__main__':
	
	obj = Solution()
	str1 = input()
	str2 = input()

	ans = obj.shortestCommonSupersequence(str1,str2)
	print(f'The shortest string that contains both str1 and str2 is : {ans}')