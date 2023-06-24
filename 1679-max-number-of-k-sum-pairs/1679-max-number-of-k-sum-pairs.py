class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        while r > l:
            sum_ = nums[l] + nums[r]
            if sum_ == k: 
                res += 1
                l += 1
                r -= 1
            elif sum_ > k: r -= 1
            else: l += 1
        return res