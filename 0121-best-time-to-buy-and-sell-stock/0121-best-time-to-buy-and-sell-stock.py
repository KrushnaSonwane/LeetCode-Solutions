class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[-1] * 2 for _ in prices]
        def dfs(i, buy, rem):
            if i == len(prices) or not rem: return 0
            if dp[i][buy] != -1: return dp[i][buy]
            if buy:
                dontSell = dfs(i + 1, buy, rem)
                sell = prices[i] + dfs(i + 1, buy, rem - 1)
            else:
                dontSell = dfs(i + 1, buy, rem)
                sell = -prices[i] + dfs(i + 1, 1, rem)
            dp[i][buy] = max(dontSell, sell)
            return dp[i][buy]
        return dfs(0, 0, 1)
