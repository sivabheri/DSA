# Subset Sum - o/1 KnapSack variation

''' 
Problem statement:
We are given an arr and a target,
we need to return either True/False ie.
if we can form a subset whose sum == Target we return True.
else we return False.

Similarity with 0/1 knapSack:
in 0/1 : we can choose a weight [pick/not] <-> here, we can/cannot make target with given element ie arr[i],
in 0/1 : capacity <-> here, target

Code variation:
base case:
1. we can form a subset with sum = 0 with array having any no of elements.
	dp[i][0] = True
2. we can never form a sum>0, with empty array.
	dp[0][j] = False
iterative code:
1. replace wt[i] with arr[i]
2. capacity with target : j
3. in 0/1, we have val[] we can neglect it here.
4. dp[i][j] = max(pick,not pick) <-> dp[i][j] = pick or(||) not pick

'''

class Solution:
    def main(self, arr, target):
        return self.tabulation(arr, target)
        # return self.recursion(arr, target, len(arr))

    def tabulation(self, arr, target):
        # Initialize variables
        n = len(arr)

        # Create a DP table initialized to False
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # Base cases
        for i in range(n + 1):
            dp[i][0] = True  # We can always form sum = 0 with an empty subset
        for j in range(1, target + 1):
            dp[0][j] = False  # Cannot form a positive sum with an empty array

        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i - 1] <= j:  # If the current element can be included
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                else:  # Exclude the current element
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]

    def recursion(self, arr, target, n):
        
        if target == 0:
            return True
        if n == 0:
            return False

        if arr[n - 1] > target:
            return self.recursion(arr, target, n - 1)

        return (self.recursion(arr, target - arr[n - 1], n - 1) or
                self.recursion(arr, target, n - 1))


# Driver code
if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        arr = list(map(int, input("Enter the array elements: ").split()))
        target = int(input("Enter the target sum: "))

        ob = Solution()
        if ob.main(arr, target):
            print("true")
        else:
            print("false")
        print("~")
