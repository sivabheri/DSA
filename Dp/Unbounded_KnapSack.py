# Un-Bounded KnapSack

'''

Same as O/1 KnapSack with one major difference.

In 0/1 : There can only one occurence of an Item.
	if an item has the chance to get into the knapsack then we only add it one time [pick]. If not we visit the next Item.[not Pick]

UnBounded : Multiple occurences of an Item.  
	
	if an item has the chance to get into the knapsack then again it may have the chance [pick/not Pick]. if not we visit the next Item.[not Pick]

o/1:  	
			ind
	  		/ \
	Processed   Not Processed
		|			|
	  ind-1		  ind-1

Unbounded:
			ind
	  		/ \
	Processed   Not Processed
		|			|
	   ind		   ind-1

Base Condition : Same in both cases.

'''

# Code Difference : 

def ks0_1(val,wt,W, n ):

	dp = [ [0]*(W+1) for _ in range(n+1) ]

	# base condition
	for i in range(n+1):
		for j in range(W+1):
			if i==0 or j==0:
				dp[i][j] = 0 

	for i in range(1,n+1):
		for j in range(1,W+1):

			if (wt[i-1] <= W ):
				# difference when we pick dp[i-1][j-arr[i-1]]
				dp[i][j] = max(val[i-1] + dp[i-1][j - wt[i-1]], dp[i-1][j])

			else:
				dp[i][j] = dp[i-1][j]

	return dp[n][W]


def unBound(val,wt,W, n ):

	dp = [ [0]*(W+1) for _ in range(n+1) ]

	# same base condition
	for i in range(n+1):
		for j in range(W+1):
			if i==0 or j==0:
				dp[i][j] = 0 


	for i in range(1,n+1):
		for j in range(1,W+1):

			if (wt[i-1] <= W ):
				# difference when we pick dp[i][j-arr[i-1]]
				dp[i][j] = max(val[i-1] + dp[i][j - wt[i-1]], dp[i-1][j])

			else:
				dp[i][j] = dp[i-1][j]

	return dp[n][W]

if __name__ == '__main__':
	
	val = [1,2,3]
	wt = [4,5,1]
	W = 4
	n = 3

	ans1 = ks0_1(val,wt,W,n)
	ans2 = unBound(val,wt,W,n)

	print(f'0/1 KnapSack : {ans1}') #4
	print(f'Unbounded KnapSack : {ans2}') #12