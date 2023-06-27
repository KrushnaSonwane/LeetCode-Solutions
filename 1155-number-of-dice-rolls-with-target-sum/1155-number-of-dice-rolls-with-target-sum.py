class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(rem, sum_):
            if sum_ > target: return 0
            if rem == 0: return int(sum_ == target)
            return sum(dfs(rem - 1, sum_ + i) for i in range(1, k + 1))
        return dfs(n, 0) % MOD