# Sorting array using recursion

def sorting(arr):

	n = len(arr)
	
	def insert_last(arr,last):
		if len(arr)==0 or arr[-1]<=last:
			arr.append(last)
			return

		cur_last = arr.pop()
		insert_last(arr,last)
		arr.append(cur_last)	
	def met(arr,n):

		if n<=1:
			return 
		last = arr.pop()
		met(arr,n-1)
		insert_last(arr,last)


	met(arr,n)

	return arr 

arr = [1,5,2,3,8,4]
new_arr = sorting(arr)
print(new_arr)