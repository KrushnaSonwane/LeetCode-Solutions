# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(low, high):
            if low==high: return [TreeNode(low)]
            if low > high: return [None]
            res = []
            for currVal in range(low, high+1):
                for leftTree in dfs(low, currVal-1):
                    for rightTree in dfs(currVal+1, high):
                        res.append(TreeNode(currVal, leftTree, rightTree))
            return res
        return dfs(1, n)