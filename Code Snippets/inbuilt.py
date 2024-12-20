
def main():
	''' Common and Helpful Inbuilt python functions'''
	# Returns the absolute value of a number
	print(abs(-10))  # Output: 10

	# Returns True if all elements are true
	print(all([True, 1, "Hello"]))  # Output: True
	print(all([True, 0, "Hello"]))  # Output: False

	# Returns True if any element is true
	print(any([False, 0, ""]))  # Output: False
	print(any([False, 1, ""]))  # Output: True

	# Converts an integer to a binary string
	print(bin(10))  # Output: '0b1010'

	# Converts values to Boolean
	print(bool(0))    # Output: False
	print(bool(1))    # Output: True
	print(bool(""))   # Output: False
	print(bool("Hi")) # Output: True

	# Converts Unicode code point to a character
	print(chr(65))  # Output: 'A'
	print(chr(97))  # Output: 'a'

	# Lists the attributes and methods of an object
	print(dir([]))  # Output: List of methods of a list

	# Enumerates over an iterable
	fruits = ["apple", "banana", "cherry"]
	for index, fruit in enumerate(fruits):
	    print(index, fruit)
	# Output:
	# 0 apple
	# 1 banana
	# 2 cherry

	# Evaluates a Python expression
	x = 10
	print(eval("x + 5"))  # Output: 15

	# Filters elements from an iterable
	numbers = [1, 2, 3, 4, 5]
	even_numbers = filter(lambda x: x % 2 == 0, numbers)
	print(list(even_numbers))  # Output: [2, 4]


	# Applies a function to all items in an iterable
	numbers = [1, 2, 3]
	squared = map(lambda x: x ** 2, numbers)
	print(list(squared))  # Output: [1, 4, 9]

	# Combines iterables into tuples
	a = [1, 2, 3]
	b = ["a", "b", "c"]
	print(list(zip(a, b)))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

if __name__ == '__main__':
	main()
	# print(main.__dict__)