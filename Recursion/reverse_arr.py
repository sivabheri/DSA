
arr = [int(i) for i in input().split()]


print("Original:",arr)
def rec_rev(arr):

	if not arr:
		return []
	last = arr.pop()
	reversed_part = rec_rev(arr)
	print(reversed_part)
	reversed_part.insert(0,last)
	return reversed_part


print("Reversed:",rec_rev(arr[:]))
print(arr)

def rec_rev2(arr):

	if not arr:
		return
	last = arr.pop()
	rec_rev2(arr)
	print(arr)
	arr.insert(0,last)
	return arr
print("Reversed:",rec_rev2(arr[:]))
print(arr)

