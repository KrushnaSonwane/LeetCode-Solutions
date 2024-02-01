# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff, res = [inf], [0]
        def dfs(root):
            if not root: return
            curr = float(max(target, root.val)-float(min(target, root.val)))
            if diff[0] > curr:
                res[0] = root.val
                diff[0] = curr
            elif diff[0] == curr:
                res[0] = min(res[0], root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res[0]