# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        A, start = {}, [None]
        hashT = defaultdict(int)
        def getval(root, parent):
            if not root:
                return 
            if root.val == startValue:
                start[0] = root
            A[root] = parent
            getval(root.left, root)
            getval(root.right, root)
        getval(root, None)
        def dfs(root, last):
            if not root: return False
            if root.val == destValue:
                hashT[root.val] = 1
                return True
            if root.left != last:
                ans = dfs(root.left, root)
                if ans:
                    hashT[root.val] = ans
                    return True
            if root.right != last:
                ans = dfs(root.right, root)
                if ans:
                    hashT[root.val] = ans
                    return ans
            if A[root] and A[root] != last:
                ans = dfs(A[root], root)
                if ans:
                    hashT[root.val] = ans
                    return ans
            return False
        dfs(start[0], None)
        Q, res = [(start[0], None)], []
        while Q:
            root, last = Q.pop(0)
            for child, d in [[root.left, 'L'], [root.right, 'R'], [A[root], 'U']]:
                if child and child != last and hashT[child.val]:
                    res.append(d)
                    Q.append((child, root))
        return ''.join(res)