# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, min_, max_):
            if not root: return 1
            if root.val >= max_ or root.val <= min_:
                return 0
            l = dfs(root.left, min_, root.val)
            r = dfs(root.right, root.val, max_)
            return l and r
        return dfs(root, float("-inf"), float("inf"))