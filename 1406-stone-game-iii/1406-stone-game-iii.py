class Solution(object):
    def stoneGameIII(self, stone):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        dp, n = {}, len(stone)
        def dfs(i):
            if i >= n: return 0
            if i in dp: return dp[i]
            ans = stone[i] - dfs(i + 1)
            if i + 1 < n:
                ans = max(ans, stone[i] + stone[i + 1] - dfs(i + 2))
            if i + 2 < n:
                ans = max(ans, stone[i] + stone[i + 1] + stone[i + 2] - dfs(i + 3))
            dp[i] = ans
            return ans
        res = dfs(0)
        return 'Alice' if res > 0 else 'Bob' if res < 0 else 'Tie'