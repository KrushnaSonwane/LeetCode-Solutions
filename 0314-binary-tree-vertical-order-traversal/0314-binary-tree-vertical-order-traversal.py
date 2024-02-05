# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashT = defaultdict(list)
        def dfs(i, j, root):
            if not root: return 
            hashT[(i, j)].append(root.val)
            dfs(i-1, j+1, root.left)
            dfs(i+1, j+1, root.right)
        dfs(0, 0, root)
        A = [i for i in sorted(hashT.keys())]
        res, last, t = [], -inf, []
        for a, b in sorted(hashT.keys()):
            if a != last:
                res.append(t)
                t = []
            for node in hashT[(a, b)]:
                t.append(node)
            last = a
        res.append(t)
        res.pop(0)
        return res