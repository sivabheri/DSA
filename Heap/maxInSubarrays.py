import heapq

def max_in_subarrays(arr, k):

	n = len(arr)
	heap = []
	res = []

	for i in range(k):
		heapq.heappush(heap,(-arr[i],i))
	res.append(-heap[0][0])

	for i in range(k,n):

		heapq.heappush(heap,(-arr[i],i))
		while heap[0][1]<= i-k:
			heapq.heappop(heap)
		res.append(-heap[0][0])
	return res
# Example usage
arr = [10, 5, 2, 7, 8, 7]
k = 3
print("Max elements in subarrays of size k:", max_in_subarrays(arr, k))
