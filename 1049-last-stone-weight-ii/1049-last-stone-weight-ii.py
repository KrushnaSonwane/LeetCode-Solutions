class Solution:
    def lastStoneWeightII(self, A: List[int]) -> int:
        @cache
        def dfs(i, f, s):
            if i == len(A): return abs(f-s)
            return min(dfs(i+1, f+A[i], s), dfs(i+1, f, s+A[i]))
        return dfs(0, 0, 0)