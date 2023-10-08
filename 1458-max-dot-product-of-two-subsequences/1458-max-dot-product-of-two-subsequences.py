class Solution:
    def maxDotProduct(self, A: List[int], B: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j, start):
            if i == len(A):
                return 0 if start else -inf
            if j == len(B):
                return 0 if start else -inf
            res = max(dfs(i+1, j, start), dfs(i, j+1, start))
            res = max(res, dfs(i+1, j+1, 1) + (A[i] * B[j]))
            return res
        return dfs(0, 0, 0)