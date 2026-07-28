# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev, slow
        curr = head
        second = prev  
        while second:
            temp = curr.next
            temp2 = second.next
            curr.next = second
            second.next = temp
            curr = temp
            second = temp2


        