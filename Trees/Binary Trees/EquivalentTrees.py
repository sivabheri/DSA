# Leetcode - 951
''' 
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

 

Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false '''

# Code:

# Definition for a binary tree node.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_order(self, arr):
        """Insert nodes into the binary tree using level order from the array."""
        if not arr:
            return None
        
        self.root = Node(arr[0])
        queue = [self.root]
        i = 1
        
        while i < len(arr):
            current = queue.pop(0)
            
            # Insert left child
            if i < len(arr) and arr[i] is not None:
                current.left = Node(arr[i])
                queue.append(current.left)
            i += 1
            
            # Insert right child
            if i < len(arr) and arr[i] is not None:
                current.right = Node(arr[i])
                queue.append(current.right)
            i += 1

class Solution:
    def flipEquiv(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False

        if root1.data != root2.data:
            return False    
        
        # Check for flip equivalence
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
    arr2 = [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]

    tree1 = BinaryTree()
    tree1.insert_level_order(arr1)

    tree2 = BinaryTree()
    tree2.insert_level_order(arr2)

    obj = Solution()
    print(obj.flipEquiv(tree1.root, tree2.root))  # Output: True

 