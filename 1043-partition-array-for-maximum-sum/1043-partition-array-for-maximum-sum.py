class Solution:
    def maxSumAfterPartitioning(self, A: List[int], k: int) -> int:
        dp = {}
        def dfs(i):
            if i not in dp:
                if i >= len(A): return 0
                res = dfs(i+1) + A[i]
                max_ = 0
                for j in range(i, min(len(A), i+k)):
                    max_ = max(A[j], max_)
                    res = max(res, dfs(j+1) + max_*(j-i+1))
                dp[i] = res
            return dp[i]
        return dfs(0)