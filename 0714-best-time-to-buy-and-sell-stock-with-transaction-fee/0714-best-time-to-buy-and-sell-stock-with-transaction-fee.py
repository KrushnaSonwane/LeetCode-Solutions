class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [[-1, -1] for _ in prices]
        def dfs(i, buy):
            if i == len(prices): return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            if buy:
                sell = prices[i] - fee + dfs(i + 1, 0)
                dontSell = dfs(i + 1, buy)
            else:
                sell = -prices[i] + dfs(i + 1, 1)
                dontSell = dfs(i + 1, buy)
            dp[i][buy] = max(dontSell, sell)
            return dp[i][buy]
        return dfs(0, 0)