class Solution:
    def numberOfPaths(self, A: List[List[int]], k: int) -> int:
        n, m, mod = len(A), len(A[0]), 10**9 + 7
        dp = [Counter() for j in range(m + 1)]
        dp[0][0] = 1
        for i, r in enumerate(A):
            for j, a in enumerate(r):
                dp[j] = Counter({(a + b) % k: c % mod for b, c in (dp[j] + dp[j-1]).items()})
        return dp[m - 1][0]