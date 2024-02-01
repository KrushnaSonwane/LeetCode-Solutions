# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return 0, inf, 0
            
            l1, l2, l3 = dfs(root.left)

            r1, r2, r3 = dfs(root.right)

            if l2 == r2 == inf:
                return 1, root.val, 1
            if l2 == inf and r2 == root.val:
                return r1 + 1, r2, r3 + 1
            if r2 == inf and l2 == root.val:
                return l1 + 1, l2, l3 + 1
            if l2 == r2 == root.val:
                return r1+l1, r2, l3+r3+1
            return 0, -inf, l3+r3
        return dfs(root)[2]