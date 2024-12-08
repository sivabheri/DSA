# Tree traversals pre-order, inorder and post. 
# Just change the logic everything will remain same
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

    def preorder_recursive(self, node):
        if node is None:
            return []
        return [node.data] + self.preorder_recursive(node.left) + self.preorder_recursive(node.right)

    def preorder_iterative(self):
        if self.root is None:
            return []
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

# Example usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Preorder Traversal (Recursive):", tree.preorder_recursive(tree.root))
print("Preorder Traversal (Iterative):", tree.preorder_iterative())