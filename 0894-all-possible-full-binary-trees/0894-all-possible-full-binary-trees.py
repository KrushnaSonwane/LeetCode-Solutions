# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n%2: return []
        if n==1: return [TreeNode()]
        res = []
        for i in range(1, n, 2):
            l = self.allPossibleFBT(i)
            r = self.allPossibleFBT(n-i-1)
            for ll in l:
                for rr in r:
                    root = TreeNode(0, ll, rr)
                    res.append(root)
        return res