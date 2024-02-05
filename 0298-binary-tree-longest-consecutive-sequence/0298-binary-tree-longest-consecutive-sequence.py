# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return inf, 0, 0
            a, b, c = dfs(root.left)
            x, y, z = dfs(root.right)
            if a - 1 == root.val == x - 1:
                return root.val, max(b, y) + 1, max(c, z, max(b, y) + 1)
            elif a - 1 == root.val:
                return root.val, b + 1, max(c, z, b + 1)
            elif x - 1 == root.val:
                return root.val, y + 1, max(c, z, y + 1)
            return root.val, 1, max(c, z, 1)
        return dfs(root)[2]