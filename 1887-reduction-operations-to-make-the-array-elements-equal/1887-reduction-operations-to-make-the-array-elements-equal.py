class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res, count = 0, 0
        for i in range(1, len(nums)):
            count += nums[i] != nums[i - 1]
            res += count
        return res