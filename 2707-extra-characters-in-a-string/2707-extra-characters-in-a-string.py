class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        hashT = {word for word in dictionary}
        dp = [-1 for _ in s]
        def dfs(i, size):
            if i == len(s): return 0
            if dp[i] != -1: return dp[i]
            min_ = dfs(i + 1, size) + 1
            for j in range(i, len(s)):
                if s[i:j + 1] in hashT:
                    min_ = min(min_, dfs(j + 1, size - (j - i) + 1))
            dp[i] = min_
            return dp[i]
        return dfs(0, len(s))