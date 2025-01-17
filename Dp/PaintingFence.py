# Painting Fence - 1D DP
'''
Given a fence with n posts and k colors,
the task is to find out the number of ways of painting the fence,
so that not more than two consecutive posts have the same color.
'''
class Solution:

	def paintways(self,n,k,dp):

		if n==1:
			return k 
		if n==2:
			return k*k 
		if dp[n]!=-1:
			return dp[n]
		# if we paint two consecutive boards (n,n-1) or any order(let n,n-2) with same colour we dont use it again
		# so remaining boards can be painted k-1 times
		way1 = self.paintways(n-1,k,dp)*(k-1) 
		way2 = self.paintways(n-2,k,dp)*(k-1) 

		dp[n] = way1+way2
		return dp[n]
	def memo(self,n,k):
		dp = [-1]*(n+1)
		return self.paintways(n,k,dp)
if __name__ == '__main__':
	
	n = int(input("Total no of boards: "))
	k = int(input("Total no of colors: "))
	
	obj = Solution()
	ans = obj.memo(n,k)
	print(f'Total no of ways to paint : {ans}')