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
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node

    def min_element(self):
        if self.root is None:
            return None
        return self._min_value_node(self.root).data

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def max_element(self):
        if self.root is None:
            return None
        return self._max_value_node(self.root).data

    def _max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def length(self):
        return self._length(self.root)

    def _length(self, node):
        if node is None:
            return 0
        return 1 + self._length(node.left) + self._length(node.right)

# Example usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Min element:", tree.min_element())
print("Max element:", tree.max_element())
print("Length:", tree.length())

tree.delete(7)
print("Length after deletion:", tree.length())