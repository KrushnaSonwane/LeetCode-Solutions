class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(i, sum_):
            if i == n:
                return 1 if sum_ == 0 else 0
            res = 0
            for num in range(1, k+1):
                if sum_ >= num:
                    res = (res + dfs(i+1, sum_ - num)) % MOD
            return res
        return dfs(0, target)