def uniquePaths(i,j,dp):

	if i==0 and j==0 :
		return 1
	if i<0 or j<0:
		return 0
	if dp[i][j]!=-1:
		return dp[i][j]
	d = uniquePaths(i-1,j,dp)
	r = uniquePaths(i,j-1,dp)

	dp[i][j] = d+r

	return dp[i][j] 

if __name__ == '__main__':
	
	m,n = map(int,input().split())

	dp = [[-1]*n for j in range(m)]
	cnt = uniquePaths(m-1,n-1,dp)

	print(cnt)