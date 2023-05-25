class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while r > l:
            if nums[l] + nums[r] == k:
                res += 1
                l += 1; r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return res