# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.found = None
        def dfs(root):
            if not root: return 
            if root.val==x: self.found = root
            dfs(root.left)
            dfs(root.right)
        
        def getSize(root):
            return 0 if not root else getSize(root.left) + getSize(root.right) + 1
        
        dfs(root)
        l = getSize(self.found.left)
        r = getSize(self.found.right)

        rem = n - (l+r+1)

        return r > l+rem+1 or l > rem+1+r or rem > l+r+1