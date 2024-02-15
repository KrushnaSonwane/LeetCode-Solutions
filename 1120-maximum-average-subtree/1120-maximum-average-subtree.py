# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = [0]
        def dfs(root):
            if not root: return 0, 0
            l, ll = dfs(root.left)
            r, rr = dfs(root.right)
            size, sum_ = l + r + 1, ll + rr + root.val
            res[0] = max(res[0], sum_ / float(size))
            return size, sum_
        dfs(root)
        return res[0]