class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        dp = [-1 for _ in range(high + 1)]
        mod = 10**9 + 7
        def dfs(length):
            if length > high: return 0
            if dp[length] != -1:
                return dp[length]
            res = int(low <= length)
            dp[length] = res + dfs(length + one) + dfs(length + zero)
            return dp[length] % mod
        return dfs(0)