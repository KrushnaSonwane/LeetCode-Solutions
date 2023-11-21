class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        res, MOD, A = 0, 10**9+7, defaultdict(int)
        for num in nums:
            sum_ = num - int(str(num)[::-1])
            res = (res + A[sum_]) % MOD
            A[sum_] += 1
        return res