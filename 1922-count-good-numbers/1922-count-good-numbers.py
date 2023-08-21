class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        @lru_cache(None)
        def dfs(n, flag):
            if n == 1: return 5 if not flag else 4
            res = (dfs(n//2, not flag) * dfs(n//2, flag)) % mod
            if n % 2: 
                res = (res * (4 if flag else 5)) % mod
            return res
        return dfs(n, False)