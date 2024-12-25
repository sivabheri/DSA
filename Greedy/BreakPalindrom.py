# Leetcode - 1328. Break Palindrom 
# Asked in Google, Amazon and GoldmanSachs  

'''
we will be given a palindormic string with all lowercase letters.
we have to replace only one character to make it not a plaindrome.
but the condition is we should replace the character with only the lexographically smallest character.

return the new string that is also lexographically smallest if replacement is possible else return empty string.

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
'''
from typing import List
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''
        
        arr = list(palindrome)
        for i in range(n//2):

            if arr[i]!='a':
                arr[i] = 'a'
                break
            
        if arr==arr[::-1]:
            if arr[-1]=='a':
                arr[-1] ='b'    
            else:
                arr[-1] = 'a'
        print("".join(i for i in arr))

if __name__ == '__main__':
	
	string = input()

	obj = Solution()

	obj.breakPalindrome(string)