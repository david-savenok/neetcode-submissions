# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = [root]
        level = []

        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr:
                    level.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            if len(level) > 0:
                res.append(level.copy())
            level.clear()
            
        return res