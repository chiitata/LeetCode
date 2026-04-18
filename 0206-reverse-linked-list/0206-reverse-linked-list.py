# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            head_next = head.next
            head.next = None
            head_next.next = head
            return head_next
        head_next = head.next
        head_next_next = head.next.next
        head.next = None
        while head_next and head_next_next:
            head_next.next = head
            head = head_next
            head_next = head_next_next
            head_next_next = head_next_next.next
        head_next.next = head
        return head_next
            
        