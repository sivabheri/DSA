# Longest substring without Repeating Characters

''' 
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
# Note : Use dictionary when we need to store last occenrences of multiple values.
# If we need to store last occurence of only one character better use Deque.
from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        cindex = {}  # we use dictionary only to store the last occurence of any character not all occurences.
        mlen = 0
        left = 0
        for right in range(len(s)):
            # if the character is previously appeared in cindex
            if s[right] in cindex:
                # we move left to the last appearead index of that character which we can get from cindex
                left = max( left, cindex[s[right]]+1 )
            # always add the current index to the dictionary
            cindex[s[right]] = right # replace if already there
            mlen = max(mlen,right-left+1)
        return mlen

        # Time Complexity : O(N)
        # Space Complexity : O(N)

if __name__ == '__main__':
    
    obj = Solution()
    s = input().strip()
    max_length = obj.lengthOfLongestSubstring(s)
    print(f'Max length of non repeating Characters : {max_length}')