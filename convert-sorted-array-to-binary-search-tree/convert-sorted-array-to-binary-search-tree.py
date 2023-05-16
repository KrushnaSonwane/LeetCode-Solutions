# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        def recur(l, r):
            if l > r:
                return None
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left, root.right = recur(l, mid-1), recur(mid+1,r)
            return root
        return recur(0, length-1)