
# Greedy algorithm to find the Min no.of Coins Required to make V

'''
 Input V let assume V as rupees 
 Condition, you can make V rupees using following coins { 1,2,5,10,20,50,100,500,1000 }
 Find the min no of coins you can take to make V rupees
'''
V = 70#int(input())
arr = [1,2,5,10,20,50,100,500,1000]

arr = arr[::-1]
cnt = 0
for i in range(len(arr)):
	
	while V >= arr[i]:
		V-=arr[i]
		cnt+=1
		pass

print(cnt)

# Note : The same problem can't solve for all the test cases. So, we use Dynamic Programming