# BFS - aka. Level Order Traversal
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def level_order(self):
        if self.root is None:
            return []
        q = deque()

        q.append(self.root)
        level = []
        while q:

        	size = len(q)
        	for i in range(size):
        		node = q.popleft()
        		level.append(node.data)
        		if node.left is not None:
        			q.append(node.left)
        		if node.right is not None:
        			q.append(node.right)
        return level


# Example usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Level order traversal is: ",tree.level_order())