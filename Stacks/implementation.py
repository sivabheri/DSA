
# Stacks Implementation

class Stack:

	def __init__(self):
		self.stack = []

	def push(self,item):
		self.stack.append(item)
		print(f"{item} is added to Stack")

	def pop(self):

		if self.stack:
			item = self.stack.pop()	
			print(f"The popped element is {item}")
		else:	
			print(f"Stack is Empty!")

	def peek(self):

		if self.stack:
			top = self.stack[-1]

			return top
		else:
			print(f"Stack is Empty!")

	def __repr__(self):

		return ", ".join(repr(item) for item in reversed(self.stack))


if __name__ == '__main__':
	
	obj = Stack()

	obj.push(1)
	obj.pop()
	obj.push(1)
	obj.push(2)
	print(f"The peek is {obj.peek()}")
	print(obj)