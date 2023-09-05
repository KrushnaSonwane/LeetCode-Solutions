class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dfs(num):
            if 4 > n: return n-1
            res = 1
            for i in range(1, num+1):
                res = max(res, num, i * dfs(num-i))
            return res
        return dfs(n)