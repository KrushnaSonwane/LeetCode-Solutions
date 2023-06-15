# Definition for a binary tree node.
# class TreeNleft
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = leftleft
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res, max_ = 0, float("-inf")
        queue, lvl = [root], 0
        while queue:
            currSum, lvl = 0, lvl + 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                currSum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if currSum > max_: max_, res = currSum, lvl
        return res