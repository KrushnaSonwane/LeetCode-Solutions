class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, sum_, l = 0, 0, 0
        for r, num in enumerate(nums):
            sum_ += num
            while num * (r - l + 1) - sum_ > k:
                sum_ -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res