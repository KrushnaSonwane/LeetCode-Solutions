# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left: return root
        hashT = {}
        res = [None]
        def dfs(root, p):
            if not root: return
            hashT[root] = p
            dfs(root.left, root)
            dfs(root.right, root)
            if root.left and not root.left.left and not root.left.right:
                res[0] = root.left
        dfs(root, None)
        ans = curr = res[0]
        while curr and hashT[curr]:
            curr.left = hashT[curr].right
            hashT[curr].left = hashT[curr].right = None
            curr.right = hashT[curr]
            hashT[curr] = None
            curr = curr.right
        return ans