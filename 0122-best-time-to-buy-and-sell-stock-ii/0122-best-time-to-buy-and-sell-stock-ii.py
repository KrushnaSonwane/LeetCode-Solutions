class Solution(object):
    def maxProfit(self, p):
        """
        One-Liner
        """
        return sum(p[i] - p[i - 1] for i in range(1, len(p)) if p[i] > p[i - 1])
        """
        Greedy Approach
        """
        res = 0
        for i in range(1, len(p)):
            if p[i - 1] < p[i]:
                res += p[i] - p[i - 1]
        return res
        """
        Recursive + DP + Memoization
        """
        dp = [[-1, -1] for _ in p]
        def dfs(i, buy):
            if i == len(p): return 0
            if dp[i][buy] != -1: return dp[i][buy]
            if buy:
                dontSell = dfs(i + 1, buy)
                sell = p[i] + dfs(i + 1, 0)
            else:
                dontSell = dfs(i + 1, buy)
                sell = -p[i] + dfs(i + 1, 1)
            dp[i][buy] = max(dontSell, sell)
            return dp[i][buy] 
        return dfs(0, 0)