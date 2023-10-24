# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res, Q = [], [root]
        while Q:
            max_ = -inf
            for _ in range(len(Q)):
                root = Q.pop(0)
                max_ = max(max_, root.val)
                for child in [root.left, root.right]:
                    if child: Q.append(child)
            res.append(max_)
        return res