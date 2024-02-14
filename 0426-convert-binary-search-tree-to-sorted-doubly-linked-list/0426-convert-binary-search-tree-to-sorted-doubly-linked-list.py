"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        A = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            A.append(root.val)
            dfs(root.right)
        dfs(root)
        res = tail = Node(-1)
        for num in A:
            curr = Node(num)
            tail.right = curr
            curr.left = tail
            tail = tail.right
        res = res.right
        res.left = tail
        tail.right = res
        return res