# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashT = defaultdict(int)
        max_ = [0]
        def dfs(root):
            if not root: return
            hashT[root.val] += 1
            max_[0] = max(max_[0], hashT[root.val])
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return [val for val in hashT if hashT[val] == max_[0]]