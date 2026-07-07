# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:       
        def dfs(p, q):
            if not p and not q:
                return True
            
            if p and q and p.val == q.val:
                left = dfs(p.left, q.left)
                right = dfs(p.right, q.right)

                if left and right:
                    return True
                    
            return False
        
        if root and subRoot:
            if root.val == subRoot.val:
                if dfs(root, subRoot):
                    return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False
        