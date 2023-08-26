class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        for num, i in zip(nums, index):
            for j in range(len(nums)-2, i-1, -1):
                res[j+1] = res[j]
            res[i] = num
        return res