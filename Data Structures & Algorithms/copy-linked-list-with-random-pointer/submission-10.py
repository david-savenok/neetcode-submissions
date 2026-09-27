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
            if curr and curr not in created.keys():
                created[curr] = Node(curr.val)
            if curr.next:
                if curr.next not in created.keys():
                    created[curr.next] = Node(curr.next.val)
                created[curr].next = created[curr.next]        
            else:
                created[curr].next = None
            if curr.random:
                if curr.random not in created.keys():
                    created[curr.random] = Node(curr.random.val)
                created[curr].random = created[curr.random]
            else:
                created[curr].random = None
            curr = curr.next
        return created[head]
        
        