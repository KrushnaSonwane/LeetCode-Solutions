# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root: return 0
            l = dfs(root.left) + 1
            r = dfs(root.right) + 1
            self.res = max(self.res, l + r - 1)
            return max(l, r)
        dfs(root)
        return self.res - 1