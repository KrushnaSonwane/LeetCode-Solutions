class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9+7
        dp = [[[-1, -1] for _ in range(3)] for i in range(n)]
        def dfs(i, late, absent):
            if late >= 3: return 0
            if i == n: return 1
            if dp[i][late][absent] != -1: return dp[i][late][absent]
            res = dfs(i+1, 0, absent) % MOD
            if not absent:
                res += dfs(i+1, 0, 1)
            res += dfs(i+1, late + 1, absent)
            dp[i][late][absent] = res % MOD
            return dp[i][late][absent]
        return dfs(0, 0, 0)