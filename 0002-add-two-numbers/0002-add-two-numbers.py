# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = 0
        l2_num = 0
        pow = 1
        while l1:
            l1_num = l1_num + l1.val * pow
            pow *= 10
            if l1.next:
                l1 = l1.next
            else:
                break
        pow = 1
        while l2:
            l2_num = l2_num + l2.val * pow
            pow *= 10
            if l2.next:
                l2 = l2.next
            else:
                break
        ans = list(str(l1_num + l2_num))
        ans_nodes = [ListNode(int(ans[0]), None)]
        for i in range(1, len(ans)):
            node = ListNode(int(ans[i]), ans_nodes[0])
            ans_nodes.insert(0, node)
        return ans_nodes[0]
        