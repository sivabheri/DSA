# Min Difference Subset Sum - (0/1 KnapSack Variation)

''' 
    Given an array arr[]  containing non-negative integers, the task is to divide it into two sets set1 and set2 
    such that the absolute difference between their sums is minimum and find the minimum difference.

Examples:

Input: arr[] = [1, 6, 11, 5]
Output: 1
Explanation: 
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11 
Hence, minimum difference is 1.  

Input: arr[] = [1, 4]
Output: 3
Explanation: 
Subset1 = {1}, sum of Subset1 = 1
Subset2 = {4}, sum of Subset2 = 4
Hence, minimum difference is 3.

Input: arr[] = [1]
Output: 1
Explanation: 
Subset1 = {1}, sum of Subset1 = 1
Subset2 = {}, sum of Subset2 = 0
Hence, minimum difference is 1.
'''
#User function Template for python3
class Solution:
    def minDifference(self, arr):
        
        # The problem is more like equal sum partition, where s1 - s2= 0
        # here, we need to find abs(s1-s2) -> min
        
        # we know that we can make a subset with 0 or more elements,
        # so, the range of subset sum is 0<=(s1,s2)<=sum(arr)
        # Then the difference will also be in the range 0<=|s1-s2|<=rangeMax
        
        # s1 + s2 = Range
        # s2 = Range - s1
        # now, we made two unknowns into one
        # So if we could find s1 then we will get s2
        
        # s1 will always lie between 0<=s1<=Range//2
        # so, we need to know the possible values of s1 in that range
        # This can be done by storing the possible values from val: 0->Range//2
        # which satisfy, subsetSum(arr,val)==True, Then we store the val in a Temp array,
        # we iterate the temp array, to get
        # min difference = s2-s1 = (Range-s1) - s1 = Range -2*s1
        
        
        n = len(arr)
        total = sum(arr)
        temp = []
        dp = [[False]*(total//2+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(total//2+1):
                if i==0:
                    dp[i][j] = False
                if j==0:
                    dp[i][j] = True
        for i in range(1,n+1):
            for j in range(1,total//2+1):
                if arr[i-1]<=j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        for val in range(total//2+1):
            if dp[n][val] == True:
                temp.append(val)
                
        ans = float('inf')
        for s1 in temp:
            ans = min(ans,total-2*s1)
            
        return ans
        

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minDifference(arr)
        print(ans)
        tc -= 1
        print("~")

