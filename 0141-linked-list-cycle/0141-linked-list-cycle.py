# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        next = head.next
        head.val = 10**6
        while next:
            if next.val == 10**6:
                return True
            next.val = 10**6
            next = next.next
        else:
            return False
            

        