
# Reverse a Stack - Using Recursion and with extra stack

class Stack:

	''' The Time complexity for Stack reversing is O(N^2)'''

	def __init__(self):
		self.stack = []

	def push(self,item):
		self.stack.append(item)
		# print(f"{item} is added to Stack")

	def pop(self):

		if self.stack:
			item = self.stack.pop()	
			# print(f"The popped element is {item}")
			return item
		else:	
			print(f"Stack is Empty!")


	def peek(self):

		if self.stack:
			top = self.stack[-1]

			return top
		else:
			print(f"Stack is Empty!")

	def reverse(self):

		if self.stack:

			x = self.pop()

			self.reverse()

			self.push_at_bottom(x)

	def push_at_bottom(self,x):

		if not self.stack:
			self.push(x)
		else:
			# first remove the last element from the stack
			temp = self.pop()

			self.push_at_bottom(x)

			self.push(temp)

	def aux_reverse(self):
		''' Time : O(N) - Space : O(N)'''
		aux_stack = Stack()
		while self.stack:
			aux_stack.push(self.pop())
		while self.aux_stack:
			self.stack.push(aux_stack.pop())

	def __repr__(self):

		return repr(self.stack)


if __name__ == '__main__':
	
	obj = Stack()

	obj.push(1)
	obj.pop()
	obj.push(1)
	obj.push(2)
	print(f"The peek is {obj.peek()}")
	print(f"Original Stack is : {obj}")
	obj.reverse()
	print(f"Reversed Stack is : {obj}")
