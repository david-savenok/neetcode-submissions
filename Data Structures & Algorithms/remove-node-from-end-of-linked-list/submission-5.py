# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        
        curr = head
        index = 1
        print(size)
        while curr and index < size - n:
            index += 1
            curr = curr.next
        print(curr.val)
        if curr == head and size - n == 0:
            head = head.next
        else:
            curr.next = curr.next.next
        return head
