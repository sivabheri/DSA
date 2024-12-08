'''To explain the maximum path sum for the binary tree represented by the array [10, 9, 20, null, null, 15, 7, -5, 25, 2, -6], we first need to construct the binary tree from this array representation.

Tree Structure
The array represents a binary tree in level order. Here’s how the tree looks when constructed:


Verify

Open In Editor
Edit
Copy code
          10
         /  \
        9    20
            /  \
           15   7
          / \   / \
        -5  25 2  -6
Explanation of the Tree
Root Node: The root of the tree is 10.
Left Subtree: The left child of 10 is 9, which has no children.
Right Subtree: The right child of 10 is 20, which has two children:
Left child 15, which has two children: -5 and 25.
Right child 7, which has two children: 2 and -6.
Maximum Path Sum Calculation
To find the maximum path sum, we will traverse the tree and calculate the maximum path sum that can be obtained from each node. The path can start and end at any node, and we will consider paths that may include both left and right children.

Starting from the Leaf Nodes:

For -5: The maximum gain is max(-5, 0) = 0 (since we only consider positive contributions).
For 25: The maximum gain is max(25, 0) = 25.
For 2: The maximum gain is max(2, 0) = 2.
For -6: The maximum gain is max(-6, 0) = 0.
Calculating Gains for Parent Nodes:

For 15:
Left gain from -5: 0
Right gain from 25: 25
Current path sum: 15 + 0 + 25 = 40
Update maximum path sum: max(-inf, 40) = 40
Return gain to parent: 15 + max(0, 25) = 40
For 7:
Left gain from 2: 2
Right gain from -6: 0
Current path sum: 7 + 2 + 0 = 9
Update maximum path sum: max(40, 9) = 40
Return gain to parent: 7 + max(2, 0) = 9
Calculating Gain for Node 20:

Left gain from 15: 40
Right gain from 7: 9
Current path sum: 20 + 40 + 9 = 69
Update maximum path sum: max(40, 69) = 69
Return gain to parent: 20 + max(40, 9) = 60
Calculating Gain for the Root Node 10:

Left gain from 9: 9
Right gain from 20: 60
Current path sum: 10 + 9 + 60 = 79
Update maximum path sum: max(69, 79) = 79
Return gain to parent: 10 + max(9, 60) = 70
Final Result
The maximum path sum for the binary tree is 79, which corresponds to the path 9 -> 10 -> 20 -> 15 -> 25. '''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        
        self.mx = float('-inf')

        def mps(root):
            
            if root is None:
                return 0
            
            lps = max(0,mps(root.left))
            rps = max(0,mps(root.right))
            
            cur_Sum = root.val + lps + rps
            self.mx = max(self.mx,cur_Sum)
            return max(lps,rps) +root.val
        mps(root)
        return self.mx

if __name__ == '__main__':
    
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    

    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)

    solution = Solution()
    print(solution.maxPathSum(root1))  # Output: 6
    print(solution.maxPathSum(root2))  # Output: 42