class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def dfs(i, j):
            if i in [-1, m] or j in [-1, n]: return 0
            if (i, j) == (m-1, n-1): return 1
            return dfs(i+1, j) + dfs(i, j+1)
        return dfs(0, 0) % (2 * (10**9))