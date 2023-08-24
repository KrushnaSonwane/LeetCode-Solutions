class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:

        @lru_cache(None)
        def dp(x, y):
            if x in [-1, m] or y in [-1, n] or A[x][y]=='0': return 0
            res = 1 + min(dp(x-1, y), dp(x, y-1), dp(x-1, y-1))
            return res

        m, n = len(A), len(A[0])
        res = max(dp(i, j) for i in range(m) for j in range(n))
        return res*res