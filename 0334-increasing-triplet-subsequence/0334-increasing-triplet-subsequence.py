class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = max(nums), max(nums)
        for num in nums:
            if first >= num:
                first = num
            elif second >= num:
                second = num
            else:
                return 1
        return 0