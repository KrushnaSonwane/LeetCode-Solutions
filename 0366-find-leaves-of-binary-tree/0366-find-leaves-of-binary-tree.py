# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        A = defaultdict(list)
        def dfs(root):
            if not root: return 0
            l = dfs(root.left)
            r = dfs(root.right)
            A[max(l, r)].append(root.val)
            return max(l, r) + 1
        max_, res = dfs(root), []
        for i in range(max_):
            res.append(A[i])
        return res