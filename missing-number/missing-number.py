class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_ = 0
        for n in nums:
            sum_ += n
        sum_2 = 0
        for i in range(1, len(nums) + 1):
            sum_2 += i
        return sum_2 - sum_