# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return [0, 0]
            l, r = dfs(root.left), dfs(root.right)
            sum_, count = root.val + l[0] + r[0], 1 + l[1] + r[1]
            if sum_ // count == root.val:
                res[0] += 1
            return [sum_, count]
        dfs(root)
        return res[0]