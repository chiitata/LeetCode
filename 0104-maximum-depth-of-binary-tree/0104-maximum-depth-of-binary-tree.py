class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 「1 + 左右の深い方の高さ」を返すだけ！
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))