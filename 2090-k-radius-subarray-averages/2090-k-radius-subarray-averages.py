class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res, sum_, size = [], 0, k * 2 + 1
        n = len(nums)
        sum_ = sum(nums[: min(k, n)])
        for i, num in enumerate(nums):
            if i + k < n: sum_ += nums[i + k]
            res.append(-1 if i - k < 0 or n <= i + k else sum_ // size)
            if i - k >= 0: sum_ -= nums[i - k]
        return res