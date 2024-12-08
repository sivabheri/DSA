from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def topView(self, root):
        if not root:
            return []

        mpp = {}
        queue = deque([(root, 0)])

        while queue:
            node, hd = queue.popleft()

            if hd not in mpp:
                mpp[hd] = node.val

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        return [mpp[hd] for hd in sorted(mpp)]

# Example usage:
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right.right = TreeNode(7)

    solution = Solution()
    print(solution.topView(root))  # Output: [4, 2, 1, 3, 6, 7]