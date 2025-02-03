# Count no of LIS in given array

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 0
        
        # Initialize the dp and count arrays
        dp = [1] * n  # Each element is at least an increasing subsequence of length 1
        count = [1] * n  # Each element has at least one LIS (itself)

        # Fill the dp and count arrays
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:  # Check if we can extend the increasing subsequence
                    if dp[j] + 1 > dp[i]:  # Found a longer subsequence
                        dp[i] = dp[j] + 1
                        count[i] = count[j]  # Reset count to count of j
                    elif dp[j] + 1 == dp[i]:  # Found another LIS of the same length
                        count[i] += count[j]  # Add the count of j to i

        # Find the maximum length of LIS
        max_length = max(dp)
        
        # Sum the counts of all LISs of maximum length
        total_count = sum(count[i] for i in range(n) if dp[i] == max_length)

        return total_count

# Example usage
solution = Solution()
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Number of Longest Increasing Subsequences is:", solution.findNumberOfLIS(nums))