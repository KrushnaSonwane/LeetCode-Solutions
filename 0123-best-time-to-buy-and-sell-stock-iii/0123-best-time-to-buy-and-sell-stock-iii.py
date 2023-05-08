class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[[-1, -1, -1] for _ in range(2)] for _ in prices]
        def dfs(i, buy, rem):
            if i == len(prices) or rem == 0: return 0
            if dp[i][buy][rem] != -1: return dp[i][buy][rem]
            if buy:
                do = prices[i] + dfs(i + 1, 0, rem - 1)
                dont = dfs(i + 1, buy, rem)
            else:
                do = -prices[i] +  dfs(i + 1, 1, rem)
                dont = dfs(i + 1, buy, rem)
            dp[i][buy][rem] = max(do, dont)
            return dp[i][buy][rem]
        return dfs(0, 0, 2)