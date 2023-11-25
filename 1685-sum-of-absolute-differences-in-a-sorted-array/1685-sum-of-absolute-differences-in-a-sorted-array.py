class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n, sum_, res = len(nums), 0, [0 for _ in nums]
        for i, num in enumerate(nums):
            sum_ += num
            res[i] = (num*(i+1)) - sum_
        sum_ = 0
        for i in range(n-1, -1, -1):
            sum_ += nums[i]
            res[i] += abs(((n - i) * nums[i]) - sum_)
        return res