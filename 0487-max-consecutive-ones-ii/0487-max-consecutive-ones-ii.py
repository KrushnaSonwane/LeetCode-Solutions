class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, i, j = 0, 0, 0
        zero = 0
        while j < len(nums):
            zero += nums[j] == 0
            while zero == 2:
                zero -= nums[i] == 0
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res