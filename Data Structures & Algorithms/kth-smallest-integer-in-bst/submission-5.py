# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 1

        def dfs(node):
            if node:
                l = dfs(node.left)
                if self.count == k:
                    self.count += 1
                    return node.val
                self.count += 1
                r = dfs(node.right)
                if l is not -1:
                    return l
                if r is not -1:
                    return r
            return -1

        return dfs(root)