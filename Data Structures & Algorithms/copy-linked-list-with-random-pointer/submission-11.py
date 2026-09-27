"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        created = {}
        curr = head
        while curr:
            created[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            created[curr].next = created[curr.next] if curr.next else None
            created[curr].random = created[curr.random] if curr.random else None
            curr = curr.next
             
        return created[head]
        
        