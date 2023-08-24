class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:

        @lru_cache(None)
        def dfs(x, y):
            if x in [-1, m] or y in [-1, n] or A[i][j]=='0': return 0
            res = 1 + min(dfs(i-1, j), dfs(i, j-1), dfs(i-1, j-1))
            return res

        m, n = len(A), len(A[0])
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res*res