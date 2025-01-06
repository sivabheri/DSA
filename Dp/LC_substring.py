# Longest Common Substring - LCS variation

''' 
We have to print the Longest common Substing in s1 and s2.
It can be done by tracking the ending index of the longest common substring.
Then the substring = any_string[starting_index->end_index]
starting_index =  end_index - Max_len(longest Common Substring) 
'''
class Solution:
    def length(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        
        # tabulation
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        # base condition
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0: # when either of the strings is empty then no LCstring
                    dp[i][j]=0
        # store the max length
        max_len = 0
        # choice diagram
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    max_len = max(max_len,dp[i][j])
                else:
                    dp[i][j] = 0 # This is the code variation with LCS, 
                    # when there is discontinuity then no common string is there 
                    # so, length is set to 0
        # for i in dp:
        # 	print(i,end='\n')
        
        return max_len

    def printLCstring(self,s1,s2):

        n = len(s1)
        m = len(s2)
        
        # tabulation
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        # base condition
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0: # when either of the strings is empty then no LCstring
                    dp[i][j]=0
        # store the max length
        max_len = 0
        end_index = 0 # ending index of the logest common substring
        # choice diagram
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    if dp[i][j]>max_len:
                        max_len = dp[i][j]
                        end_index = i
                else:
                    dp[i][j] = 0 # Discontinuity        
        startInd = end_index - max_len
        string = s1[startInd:end_index]
        return string 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = 1
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(f'The Length of Longest common Substring is : {ob.length(S1, S2)}')
        print(f'The Longest common Substring is: {ob.printLCstring(S1,S2)}')

# } Driver Code Ends