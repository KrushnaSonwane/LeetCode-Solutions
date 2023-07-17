# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        hashT = defaultdict(int)
        def dfs(root):
            if not root: return 0
            l = dfs(root.left)
            r = dfs(root.right)
            sum_ = root.val + l + r
            hashT[sum_] += 1
            return sum_
        dfs(root)
        max_, res = max(hashT.values()), []
        for val in hashT:
            if hashT[val] == max_: res.append(val)
        return res