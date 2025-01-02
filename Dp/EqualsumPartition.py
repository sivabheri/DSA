# Equal Sum Partition - 0/1 knapSack variation

''' Given an array arr[], 
 return true if it can be partitioned into two subsets such that the sum of elements in both parts is the same,
 otherwise, false.
Elements should be partitioned such that the each element is used exactly once in each partition.

Examples:

Input: arr = [1, 5, 11, 5]
Output: true
Explanation: The two parts are [1, 5, 5] and [11].
Input: arr = [1, 3, 5]
Output: false
Explanation: This array can never be partitioned into two such parts.'''

class Solution:
    def equalPartition(self, arr):
        # code here
        n = len(arr)
        
        if sum(arr)%2!=0:
            return False
        
        return self.subsetSum(arr,sum(arr)//2,n)
    
    def subsetSum(self,arr,target,n):
        
        # tabulation
        
        dp = [[False]*(target+1) for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(target+1):
                # to get sum = 0 we can always have an array (empty subset)
                if (j==0):
                    dp[i][j] = True
                # if no elements in arr n==0 we cannot get sum >0
                if (i==0):
                    dp[i][j] = False
                
        
        for i in range(1,n+1):
            for j in range(1,target+1):
                
                if (arr[i-1]<=j) :
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]

if __name__ == '__main__':
	
	arr = [int(i) for i in input().split()]

	obj = Solution()

	print(f'Possible for equal Partioning ? {obj.equalPartition(arr)}')