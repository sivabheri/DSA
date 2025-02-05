# Find length of the longest subarray containing atmost two distinct integers
# Difficulty: Medium Accuracy: 47.98%  Average Time: 30m

'''
Given an array arr[] containing positive elements, the task is to find the length of the longest subarray of an input array containing at most two distinct integers.

Examples:

Input: arr[]= [2, 1, 2]
Output: 3
Explanation: The entire array [2, 1, 2] contains at most two distinct integers (2 and 1). 
Hence, the length of the longest subarray is 3.

Input: arr[] = [3, 1, 2, 2, 2, 2]
Output: 5
Explanation: The longest subarray containing at most two distinct integers is [1, 2, 2, 2, 2], which has a length of 5. 
The subarray starts at the second element 1 and ends at the last element. It contains at most two distinct integers (1 and 2).

'''
#User function Template for python3
from collections import defaultdict

class Solution:
    def totalElements(self, arr):
        left = 0
        mlen = 0
        indmap = {}  # To store the last occurrence of each distinct element
        
        for right in range(len(arr)):
            # Add the current element to the map
            indmap[arr[right]] = right
            
            # If the number of distinct elements exceeds 2
            while len(indmap) > 2:
                # Find the leftmost index of the first distinct element
                first_item = min(indmap, key=indmap.get)  # Get the element with the smallest index
                left = indmap[first_item] + 1  # Move left pointer after the last occurrence of the first distinct element
                del indmap[first_item]  # Remove it from the map
            
            # Update the maximum length found
            mlen = max(mlen, right - left + 1)
        
        return mlen
        
        #         Time Complexity: (O(N))

        # Each element is processed at most twice 
        # (once by the right pointer and potentially once by the left pointer).

if __name__ == '__main__':
    t = 1
    for _ in range(t):
        # N = int(input())
        arr = [3, 1, 2, 2, 2, 2]
        ob = Solution()
        res = ob.totalElements(arr)
        print(res)
        print("~")

# } Driver Code Ends