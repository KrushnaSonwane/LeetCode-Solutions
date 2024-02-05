# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        res = [inf, None]
        def dfs(root):
            if not root: return
            if root.val > p.val:
                if res[0] > root.val:
                    res[0], res[1] = root.val, root
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return None if res[0] == inf else res[1]