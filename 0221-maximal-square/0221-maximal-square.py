class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:

        @lru_cache(None)
        def dp(x, y):
            if x in [-1, m] or y in [-1, n] or A[i][j]=='0': return 0
            res = 1 + min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1))
            return res

        m, n = len(A), len(A[0])
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dp(i, j))
        return res*res