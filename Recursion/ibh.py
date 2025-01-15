# Starting recursion from the beginning

''' 
Methods:
1 . IBH : Induction - Base Condition - Hypothesis
2 . IP-OP
3 . Choice Diagram



'''

# Program to print 1 to n numbers

''' 
Hypothesis : 
fun(n) -> prints 1 2 3 4 .. n
fun(n-1) -> prints 1 2 3 4 .. n-1
Therefore, fun(n) -> fun(n-1) + print(n)
'''
def solve1(n):

	# Base Condition : 
	# two ways : 1. Think of Smallest valid input
	# # 2. Think of Smallest invalid input

	# if n==1: # valid input
	# 	print(1,end =' ')
	# 	return
	
	if n==0: # Smallest invalid input
		return
	
	# call fun(n-1)
	solve1(n-1)

	# if fun(n-1) function finished ie., is called it returns some thing 
	# Then we will finsh the pending work
	print(n,end = ' ')

solve1(10)
