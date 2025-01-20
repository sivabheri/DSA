# General Recursive Approach for most of the tree problem

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None 
		
def solve(root,ans):

	# base condition
	if not root:
		return 0 # or T/F based on the return type

	# get the answer from left node and right node
	leftans = solve(root.left,ans)
	rightans = solve(root.right,ans)

	# temp ans will be from either left node or right node but not both
	tempans = max(leftans,rightans) + 1 # adding 1 is because we include the root

	# update the global result based on answer we get from this node
	curans = leftans + rightans + 1
	ans = max(ans,curans)
	return tempans # because the final answer will be from left or right branch and it will be stored in temp 
	# so temp ans will be retured to the root function call

def main():

	root = Node(6)
	root.left = Node(7)
	root.right = Node(10)
	root.left.right = Node(20)
	root.left.left = Node(-10)
	root.right.left = Node(5)


	# initialize req ans
	ans = float('inf')

	# call function on the root node
	res = solve(root,ans)

	# return final ans 
	print(res)

if __name__ == '__main__':
	main()