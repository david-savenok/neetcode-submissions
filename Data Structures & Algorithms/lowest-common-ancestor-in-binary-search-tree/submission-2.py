# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        lca = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
                lca = curr
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
                lca = curr
            else:
                break

        return lca