import heapq

# Min-Heap
min_heap = [2,3,8,1,2]
heapq.heapify(min_heap)

print('Min Heap: ',*min_heap)
# Pushing an element
heapq.heappush(min_heap,0)
print('Min Heap: ',*min_heap)
#Deletion
element = heapq.heappop(min_heap)
print('Minimum element With Poping: ',element)
print('Min Heap: ',*min_heap)
print()

# Max-Heap
max_heap = [2,3,8,-1,2]
max_heap = list(map(lambda x:x*(-1),max_heap))
heapq.heapify(max_heap)
print('Max Heap: ',*max_heap)
# Pushing an element
heapq.heappush(min_heap,0)
print('Max Heap: ',*max_heap)
#Deletion
element = heapq.heappop(max_heap)
print('Maximum element With Poping: ',-1*element)
print('Max Heap: ',*max_heap)
