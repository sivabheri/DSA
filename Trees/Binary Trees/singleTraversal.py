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

    def dfs_traversal(self):
        if self.root is None:
            return [], [], []
        
        stack = [(self.root, 0)]
        preorder, inorder, postorder = [], [], []

        while stack:
            node, state = stack.pop()

            if state == 0:  # Preorder
                preorder.append(node.data)
                stack.append((node, 1))  # Move to Inorder
                if node.left:
                    stack.append((node.left, 0))  # Go to left child
            elif state == 1:  # Inorder
                inorder.append(node.data)
                stack.append((node, 2))  # Move to Postorder
                if node.right:
                    stack.append((node.right, 0))  # Go to right child
            else:  # Postorder
                postorder.append(node.data)

        return preorder, inorder, postorder

# Example usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

preorder, inorder, postorder = tree.dfs_traversal()
print("Preorder Traversal:", preorder)
print("Inorder Traversal:", inorder)
print("Postorder Traversal:", postorder)