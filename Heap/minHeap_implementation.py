class MinHeap(object):
	"""docstring for MinHeap
		
   The Heaps use dynamic memory allocation
   The have a complete Binary Tree structure.
   Insertion = O(LogN)
   Deletion / getting Min element = O(N LogN)
   Peek = O(1)
	   
	   Summary of Use Cases
Priority Queues: Efficiently manage tasks based on priority.
Dynamic Sorting: Maintain a sorted order in a changing dataset.
Graph Algorithms: Optimize pathfinding and minimum spanning tree calculations.
Merging Lists: Speed up the process of combining sorted data.
Memory Management: Efficiently allocate and deallocate memory.
Real-Time Systems: Ensure timely responses in critical applications.
	"""
	def __init__(self):
		self.heap = []

	def parent(self,index):
		return (index-1) // 2

	def left_child(self,index):
		return 2*index + 1

	def right_child(self,index):
		return 2*index + 2

	def insert(self,key):
		self.heap.append(key)
		self._heapify_up(len(self.heap)-1)
		print(*self.heap,end ='\n')

	def _heapify_up(self,index):

		while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
			self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
			index = self.parent(index)

	def get_min(self):
		if len(self.heap) == 0:
			return None

		if len(self.heap) == 1:
			return self.heap.pop()

		root = self.heap[0]
		self.heap[0] = self.heap.pop()
		self._heapify_down(0)
		# print(*self.heap,end='\n')
		return root

	def _heapify_down(self,index):

		smallest = index
		left = self.left_child(index)
		right = self.right_child(index)

		if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
			smallest = left 
		if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
			smallest = right 

		if smallest!=index:
			self.heap[index],self.heap[smallest] = self.heap[smallest],self.heap[index]
			self._heapify_down(smallest)


	def peek(self):
		return self.heap[0] if self.heap else None

	def is_empty(self):
		return len(self.heap) == 0

	def size(self):
		return len(self.heap)

if __name__ == '__main__':
	
	mhp = MinHeap()
	mhp.insert(6)
	mhp.insert(4)
	mhp.insert(5)
	mhp.insert(8)
	mhp.insert(2)
	mhp.insert(1)
	print("Minimum element removed:", mhp.get_min())
	print("Heap after removal:", mhp.heap)
	# print(mhp.__doc__)