# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    count = 0
    def dfs(self, root, arr):
        if not root: return
        arr[root.val] += 1
        self.dfs(root.left, arr)
        self.dfs(root.right, arr)
        if root.left is None and root.right is None:
            flag = 0
            for i in range(1, 10):
                if arr[i] % 2 == 1: flag += 1
            if 1 >= flag: self.count += 1
        arr[root.val] -= 1
        
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr = [0] * 10
        self.dfs(root, arr)
        return self.count