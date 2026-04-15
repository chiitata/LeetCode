# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_seen = set()
        current = head
        ind = 0
        while current:
            if current is not None:
                if current in node_seen:
                    return current
                node_seen.add(current)
                current = current.next
        else:
            return None
        