class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            nums[i].sort()
        for i in range(len(nums[0])):
            max_ = 0
            for j in range(len(nums)):
                max_ = max(max_, nums[j][i])
            res += max_
        return res