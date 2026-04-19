# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        que = deque()
        que.append((root, 1))
        while que:
            leaf, count = que.popleft()
            if leaf is None:
                continue
            if leaf.left == None and leaf.right == None:
                return count
            else:
                que.append((leaf.right, count+1))
                que.append((leaf.left, count+1))
        return 0