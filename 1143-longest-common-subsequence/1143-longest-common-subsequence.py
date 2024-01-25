class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        @cache
        def dfs(i, j):
            if len(A) == i: return 0
            if len(B) == j: return 0
            if A[i] == B[j]:
                return dfs(i+1, j+1) + 1
            return max(dfs(i+1, j), dfs(i, j+1))
        return dfs(0, 0)