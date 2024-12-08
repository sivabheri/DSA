class Queue(object):
	"""docstring for Queue - FIFO"""
	def __init__(self, size):
		
		self.size = size
		self.front = -1
		self.rear = -1

		self.queue = [None]*self.size

	def isFull(self):

		return (self.front == (self.rear + 1)) or ((self.rear+1) == self.size)
		
	def isEmpty(self):
		return self.front == -1


	def enqueue(self,num):

		if self.isFull():
			return f"Queue is Full to enqueue!"
		
		if self.isEmpty():
			self.front = 0
			self.rear = 0
		else:
			self.rear +=1
		self.queue[self.rear] = num

	def dequeue(self):

		if self.isEmpty():
			return f"Queue is Empty to delete!"

		if self.front == self.rear:
			self.font = self.rear = -1
		else:
			self.queue[self.front] = None
			self.front +=1

	def Size(self):

		if self.isEmpty():
			return 0
		elif self.isFull():
			return self.size

		else:
			return self.rear - self.front + 1

	def __str__(self):
		if not self.isEmpty():
			return str(self.queue[self.front:self.rear+1])
		return "Empty Queue"
if __name__ == '__main__':
	
	q = Queue(6)

	q.enqueue(1)
	q.enqueue(6)
	q.enqueue(4)
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(5)
	q.dequeue()
	print(f"Elements of Queue are: {q}")

	print(q.__doc__)