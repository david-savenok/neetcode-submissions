# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def _isValidBST(root, l, r):
            if not root:
                return True
            if root.val >= r:
                return False
            if root.val <= l:
                return False
            
            return _isValidBST(root.left, l, root.val) and _isValidBST(root.right, root.val, r)
        
        return _isValidBST(root, -10000000000, 10000000000)