class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        @cache
        def dfs(i, j, k):
            if i == -1 or i == m or j == -1 or j == n: return 1
            if k == 0: return 0
            res = 0
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                res = (res + dfs(x, y, k - 1)) % MOD
            return res
        return dfs(startRow, startColumn, maxMove)