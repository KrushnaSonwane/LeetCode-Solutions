class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for buy in range(0, 2):
                if buy:
                    dontSell = -prices[i] + dp[i  + 1][0]
                    sell = dp[i + 1][1]
                else:
                    dontSell = prices[i] + dp[i + 1][1]
                    sell = dp[i + 1][0]
                dp[i][buy] = max(dontSell, sell)
        return dp[0][1]