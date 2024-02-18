# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(root, i):
            if not root:
                return i == len(arr)
            if i == len(arr)-1:
                if root.val == arr[i] and not root.left and not root.right: return True
                return False
            if i == len(arr): return False
            res = False
            if root.val == arr[i]:
                res = dfs(root.left, i + 1) or dfs(root.right, i + 1)
            return res
        return dfs(root, 0)