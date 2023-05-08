class Solution(object):
    def maxProfit(self, prices):
        """
        Greedy Approach
        """
        res = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                res += prices[i] - prices[i - 1]
        return res
        """
        Recursive + DP + Memoization
        """
        dp = [[-1, -1] for _ in prices]
        def dfs(i, buy):
            if i == len(prices): return 0
            if dp[i][buy] != -1: return dp[i][buy]
            if buy:
                dontSell = dfs(i + 1, buy)
                sell = prices[i] + dfs(i + 1, 0)
            else:
                dontSell = dfs(i + 1, buy)
                sell = -prices[i] + dfs(i + 1, 1)
            dp[i][buy] = max(dontSell, sell)
            return dp[i][buy] 
        return dfs(0, 0)