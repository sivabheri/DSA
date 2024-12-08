
# Stack using arrays - C++ version of Pyton code

class Stack:

	def __init__(self,size):
		self.size = size
		self.top = -1
		self.arr = [0]*size


	def push(self,num):
		if self.top == self.size:
			return f" Stack is Full - Stack OverFlow"
		self.top+=1
		self.arr[self.top] = num

	def pop(self):
		if self.top == -1:
			return f" Stack is Empty - Stack UnderFlow"
		x = self.arr[self.top]
		self.arr[self.top] = 0
		self.top -=1
		return x

	def _top(self):
		return self.arr[self.top]

	def _size(self):
		return self.top + 1

	def __str__(self):
		return str(self.arr[:self.top+1])

if __name__ == '__main__':
	
	s = Stack(5)

	s.push(1)
	s.push(5)
	s.push(6)
	s.pop()
	print(s)
	print(f"Current Stack size: {s._size()}")
	print(f"Stack Top is : {s._top()}")
	# print(f'The stack has {s.size()} elements')

