class Solution:
    def maximumSum(self, A: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, start, end, delete):
            if i == len(A):
                return 0 if start else -inf
            if end: return 0
            if not start:
                res = dfs(i+1, start, end, delete)
                res = max(res, A[i] + dfs(i+1, 1, end, delete))
            else:
                res = A[i] + dfs(i+1, start, end, delete)
                if not delete:
                    res = max(res, dfs(i+1, start, end, 1))
                res = max(res, A[i] + dfs(i+1, start, 1, delete))
            return res
        return dfs(0, 0, 0, 0)