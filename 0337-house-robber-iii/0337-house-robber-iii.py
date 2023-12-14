# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(root, last):
            if not root: return 0
            if last:
                res = dfs(root.left, 0) + dfs(root.right, 0)
            else:
                res = max(dfs(root.left, 0) + dfs(root.right, 0), dfs(root.left, 1) + dfs(root.right, 1)+root.val)
            return res
        return dfs(root, 0)