# Fractional Knapsack problem 
# using Greedy approach

# input : arr : [values] , weights : [weight of each value] , W = capacity of Knapsack
# find the max total of values after filling the Knapsack

# Logic
def Knapsack(arr,weights,w):
	n = len(arr)
	indices = list(range(n))

	indices.sort(key = lambda x : arr[x]//weights[x],reverse = True)
	curWeight = 0
	curVal = 0.0 
	for i in indices:

		if curWeight+weights[i] <= w:
			curWeight+=weights[i]
			curVal+=arr[i]
		else:
			remain = w - curWeight
			curVal += remain * (arr[i]/weights[i])
			break



	return indices


# Main Function
# arr = [int(i) for i in input().split()]
# weights = [int(i) for i in input().split()]
# w = int(input())
arr = [60,120,100,40]
weights = [10,30,20,10]
w = 50
Tval = Knapsack(arr,weights,w)
print("Total Value of Knapsack : ",Tval)