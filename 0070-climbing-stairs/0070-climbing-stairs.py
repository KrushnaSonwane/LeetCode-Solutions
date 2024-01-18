class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i > n: return 0
            if i == n: return 1
            return dfs(i+1) + dfs(i+2)
        return dfs(0)