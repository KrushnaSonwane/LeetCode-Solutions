class Solution:
    def minDistance(self, S1: str, S2: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == len(S1): return len(S2) - j
            if j == len(S2): return len(S1) - i
            if S1[i] == S2[j]:
                return dfs(i+1, j+1)
            return min(dfs(i+1, j), dfs(i, j+1)) + 1
        return dfs(0, 0)