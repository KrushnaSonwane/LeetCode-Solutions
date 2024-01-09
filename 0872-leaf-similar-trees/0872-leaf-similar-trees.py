# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        A, B = [], []
        
        def dfs1(root):
            if not root: return
            if not root.left and not root.right:
                A.append(root.val)
                return
            dfs1(root.left)
            dfs1(root.right)
        def dfs2(root):
            if not root: return
            if not root.left and not root.right:
                B.append(root.val)
                return
            dfs2(root.left)
            dfs2(root.right)
        dfs1(root1); dfs2(root2)
        
        return A == B