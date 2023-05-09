# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(r1, r2):
            if not r1 and not r2: return 1
            if (not r1 and r2) or (not r2 and r1): return 0
            if r1.val != r2.val: return 0
            return dfs(r1.left, r2.right) and dfs(r1.right, r2.left)
        return dfs(root.left, root.right)