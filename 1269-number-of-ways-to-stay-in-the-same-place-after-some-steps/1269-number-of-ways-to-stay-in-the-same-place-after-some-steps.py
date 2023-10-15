class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(i, pos):
            if i == steps:
                return 1 if pos == 0 else 0
            if pos == -1: return 0
            if pos == arrLen: return 0
            res = (dfs(i+1, pos) + dfs(i+1, pos+1) + dfs(i+1, pos-1)) % MOD
            return res
        return dfs(0, 0)