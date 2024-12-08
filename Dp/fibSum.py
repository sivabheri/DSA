
def fibSum(i,dp):

	if i<=1:
		return i 
	if dp[i]!=-1:
		return dp[i]

	dp[i] = fibSum(i-1,dp)+fibSum(i-2,dp)
	return dp[i]


if __name__ == '__main__':
	

	n = int(input())
	# dp = [-1]*(n+1)
	prev = 0
	prev2 = 1
	addn = 1
	# addn = dp[0]+dp[1]
	for i in range(2,n):
		cur = prev+prev2
		prev2 = prev
		prev = cur
		addn+= prev
		
	addn+=prev
	# addn = 0
	# for i in range(n):
	# 	addn+=fibSum(i,dp)
	# addn = fibSum(n)

	print(addn)