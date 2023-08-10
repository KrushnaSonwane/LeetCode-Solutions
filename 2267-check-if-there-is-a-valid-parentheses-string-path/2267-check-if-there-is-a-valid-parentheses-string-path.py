class Solution:
    def hasValidPath(self, A: List[List[str]]) -> bool:
        m, n = len(A), len(A[0])
        @lru_cache(None)
        def dfs(i, j, k):
            if 0 > k: return False
            if i == m-1 and j == n-1:
                return k==1 and A[i][j]==')'
            res = False
            k += (1 if A[i][j]=='(' else -1)
            for x, y in [(i+1, j), (i, j+1)]:
                if x == m or y == n: continue
                res = dfs(x, y, k) or res
            return res
        return dfs(0, 0, 0)