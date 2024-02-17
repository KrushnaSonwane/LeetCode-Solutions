class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        sum_, res, j = 0, 0, 0
        MOD = 10**9+7
        A = Counter()
        for i, num in enumerate(nums):
            if A[num] != 0:
                sum_ -= pow(num, A[num], MOD)
            A[num] += 1
            sum_ += pow(num, A[num], MOD)
            if i >= k-1:
                res = max(res, sum_%MOD)
                sum_ -= pow(nums[j], A[nums[j]], MOD)
                A[nums[j]] -= 1
                if A[nums[j]] != 0:
                    sum_ += pow(nums[j], A[nums[j]], MOD)
                j += 1
        return res