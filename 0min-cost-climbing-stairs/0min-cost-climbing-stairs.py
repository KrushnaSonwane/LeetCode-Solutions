class Solution:
    def minCostClimbingStairs(self, A: List[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(A): return 0
            res = min(dfs(i+1), dfs(i+2)) + A[i]
            return res
        return min(dfs(0), dfs(1))