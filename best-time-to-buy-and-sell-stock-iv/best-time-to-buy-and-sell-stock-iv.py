class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        dp = [[[-1 for _ in range(k + 1)] for _ in range(2)] for _ in prices]
        def dfs(i, buy, rem):
            if i == len(prices) or rem == 0: return 0
            if dp[i][buy][rem] != -1: return dp[i][buy][rem]
            if buy:
                dont = dfs(i + 1, buy, rem)
                do = prices[i] + dfs(i + 1, 0, rem - 1)
            else:
                dont = dfs(i + 1, buy, rem)
                do = -prices[i] + dfs(i + 1, 1, rem)
            dp[i][buy][rem] = max(dont, do)
            return dp[i][buy][rem]
        return dfs(0, 0, k)