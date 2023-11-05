class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        A = []
        for num, D in zip(nums, s):
            A.append(num + (d if D == 'R' else -d))
        A.sort()
        res, MOD, sum_ = 0, 10**9+7, 0
        for i in range(1, len(A)):
            sum_ = sum_ + (abs(A[i]-A[i-1]) * i)
            res = (res + sum_) % MOD
        return res

