# Minimum Jumps
# Difficulty: MediumAccuracy: 11.91%Submissions: 976K+Points: 4

'''
You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

For example:

If arr[i] = 3, you can jump to index i + 1, i + 2, or i + 3 from position i.
If arr[i] = 0, you cannot jump forward from that position.
Your task is to find the minimum number of jumps needed to move from the first position in the array to the last position.

Note:  Return -1 if you can't reach the end of the array.

Examples : 

Input: arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3 
Explanation: First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last. 
Input: arr = [1, 4, 3, 2, 6, 7]
Output: 2 
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
Input: arr = [0, 10, 20]
Output: -1
Explanation: We cannot go anywhere from the 1st element.'''

class Solution:
    def minJumps(self, arr):
        # Length of the array
        n = len(arr)

        # Recursive function with memoization
        def recursive(ind):
            # Base case: when we are at n-1 or crossed, we don't need to make any step
            if ind >= n - 1:
                return 0

            if dp[ind] != -1:
                return dp[ind]

            total = float('inf')

            # Explore all possible jumps from the current index
            for nextstep in range(ind + 1, arr[ind] + ind + 1):
                # This recursive call runs until it reaches or crosses the base condition
                jumps = recursive(nextstep)

                if jumps != float('inf'):
                    total = min(total, 1 + jumps)

            dp[ind] = total
            return dp[ind]

        dp = [-1] * n
        dp[n - 1] = 0  # No jumps needed when we are already at the last index

        # Start recursion from the first index
        ans = recursive(0)

        # If it's not possible to reach the last index, return -1
        if ans == float('inf'):
            return -1

        return ans

        """
        Time Complexity:
        - Each index is processed only once due to memoization, making the recursion depth O(N).
        - In the worst case, each index could check up to N steps ahead, resulting in O(N^2).

        Space Complexity:
        - Recursion stack space is O(N) due to the depth of the recursion.
        - The dp array also takes O(N) space.
        - Therefore, overall space complexity is O(N).
        """
    def minJumps2(self, arr):
        n = len(arr)
        
        if n == 1:
            return 0

        if arr[0] == 0:
            return -1

        dp = [float('inf')] * n
        dp[0] = 0  # No jumps needed to stay at the first index
        
        for i in range(n):
            # Check all indices reachable from index i
            for j in range(1, arr[i] + 1):
                if i + j < n:
                    dp[i + j] = min(dp[i + j], dp[i] + 1)

        # If last index is still infinity, that means it’s not reachable
        return dp[n - 1] if dp[n - 1] != float('inf') else -1

# Example usage
if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    sol = Solution()
    print("Minimum jumps to reach the end:", sol.minJumps2(arr))  # Expected Output: 3

