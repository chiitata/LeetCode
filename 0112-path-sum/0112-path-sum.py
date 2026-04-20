# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, target):
            if root is None:
                return False
            val = root.val + target
            if val == targetSum and root.right is None and root.left is None:
                return True
            left = helper(root.left, root.val + target)
            right = helper(root.right, root.val + target)
            return left or right
        return helper(root, 0)