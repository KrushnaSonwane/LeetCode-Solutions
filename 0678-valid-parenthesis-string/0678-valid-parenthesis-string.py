class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dp = [[-1 for _ in s] for _ in s]
        def dfs(i, rem):
            if i == len(s): return rem == 0
            if dp[i][rem] != -1: return dp[i][rem]
            if s[i] == '(':
                ans = dfs(i + 1, rem + 1)
            elif s[i] == ')':
                ans = rem != 0 and dfs(i + 1, rem - 1)
            else:
                ans = (rem != 0 and dfs(i + 1, rem - 1)) or dfs(i + 1, rem + 1) or dfs(i + 1, rem)
            dp[i][rem] = ans
            return ans
        return dfs(0, 0)