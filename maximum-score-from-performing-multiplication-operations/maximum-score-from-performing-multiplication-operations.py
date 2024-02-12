class Solution:
    def maximumScore(self, A: List[int], B: List[int]) -> int:
        @cache
        def dfs(i, j, k):
            if k == len(B): return 0
            res = max(dfs(i+1, j, k+1) + B[k] * A[i], dfs(i, j-1, k+1) + B[k] * A[j])
            return res
        return dfs(0, len(A)-1, 0)