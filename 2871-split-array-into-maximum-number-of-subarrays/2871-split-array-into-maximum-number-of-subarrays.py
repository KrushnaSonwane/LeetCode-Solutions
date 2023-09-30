class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        AND = nums[0]
        for num in nums:
            AND &= num
        if AND: return 1
        res, AND = 0, nums[0]
        for num in nums:
            if AND == inf:
                AND = num
            AND &= num
            if AND == 0:
                res += 1
                AND = inf
        return res