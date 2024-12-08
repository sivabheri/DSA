# Longest Palindrome in a String

# Method 1 : Naive Approach

class Palindrome:

	def checkPalindrome(self,s,low,high):

		while (low<high):

			if s[low]!=s[high] :
				return False
			low+=1
			high-=1

		return True

	def method1(self,s): # TC : O(N3) SC : O(1)

		start = 0
		max_length = 1 

		for i in range(len(s)):

			for j in range(i,len(s)):

				if self.checkPalindrome(s,i,j) and j-i+1 > max_length:
					start = i 
					max_length = j - i + 1
		return s[start:start+max_length] 


	def method2(self,s): # TC : O(N2) SC : O(N2)
		# Using Dp
		n = len(s)
		dp = [[False] * n for _ in range(n)]
		# All substrings of length 1 are palindromes
		max_len = 1
		for i in range(n):
		    dp[i][i] = True
		# Check for sub-string of length 2

		start = 0
		for i in range(n - 1):
		    if s[i] == s[i + 1]:
		        dp[i][i + 1] = True
		        start = i
		        max_len = 2

		for k in range(3, n + 1):
			for i in range(n - k + 1):
				j = i + k - 1
				if dp[i + 1][j - 1] and s[i] == s[j]:
					dp[i][j] = True
					if k > max_len:
						start = i
						max_len = k

		return s[start:start + max_len]



if __name__ == '__main__':
	obj = Palindrome()
	s = input("Enter a string: ")
	print("Longest Palindromic Substring:", obj.method2(s))
