# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        que.append((root, 0))
        ans = defaultdict(list)
        while que:
            node = que.pop()
            a, level = node
            if a is None:
                continue
            ans[level].append(a.val)
            if a.right or a.left:
                if a.right and a.left:
                    que.append((a.right, level+1))
                    que.append((a.left, level+1))
                else:
                    newnode = a.right or a.left
                    que.append((newnode, level+1))
        ans = list(ans.values())
        for i in range(len(ans)):
            if i%2 == 1:
                ans[i] = ans[i][::-1]
        return ans