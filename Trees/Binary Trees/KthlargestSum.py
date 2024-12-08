# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root, k):
        from collections import deque
        q = deque()
        rt = TreeNode(root[0])
        q.append(rt)

        level = []
        res = float('-inf')
        while q:
            size = len(q)
            res = 0
            for i in range(size):
                last_node = q.popleft()
                res += last_node.val
                
                if last_node.left:
                    q.append(last_node.left)
                if last_node.right:
                    q.append(last_node.right)
            level.append(res)
        level=sorted(level,reverse=True)
        return level[k] if k<=len(level) else -1

if __name__ == '__main__':

    root = [5,8,9,2,1,3,7,4,6]
    k = 2
    obj = Solution()
    res = obj.kthLargestLevelSum(root,k)
    print(res)