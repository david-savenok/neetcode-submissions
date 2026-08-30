# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.elems = []

        def dfs(node):
            if node:
                dfs(node.left)
                self.elems.append(node.val)
                dfs(node.right)
        
        dfs(root)
        return self.elems[k - 1]