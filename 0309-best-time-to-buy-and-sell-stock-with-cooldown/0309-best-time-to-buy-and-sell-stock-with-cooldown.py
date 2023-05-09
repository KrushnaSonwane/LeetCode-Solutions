class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[[-1, -1] for _ in range(2)] for _ in prices]
        def dfs(i, buy, cool):
            if i == len(prices): return 0
            if dp[i][buy][cool] != -1: return dp[i][buy][cool]
            if buy:
                sell = prices[i] + dfs(i + 1, 0, 1)
                dontSell = dfs(i + 1, buy, cool)
            else:
                if cool:
                    sell = 0
                    dontSell = dfs(i + 1, buy, cool - 1)
                else:
                    dontSell = dfs(i + 1, buy, cool)
                    sell = -prices[i] + dfs(i + 1, 1, cool)
            dp[i][buy][cool] = max(sell, dontSell)
            return dp[i][buy][cool]
        return dfs(0, 0, 0)