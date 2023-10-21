# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0, 0, 0]
            l, r = dfs(root.left), dfs(root.right)
            sum_, count, res = root.val + l[0] + r[0], 1 + l[1] + r[1], l[2] + r[2]
            if sum_ // count == root.val:
                res += 1
            return [sum_, count, res]
        return dfs(root)[2]