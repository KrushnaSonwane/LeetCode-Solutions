class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(i):
            if i >= n: return 1
            return (dfs(i+1) + dfs(i+2)) % MOD
        res = dfs(0)
        return (res * res) % MOD