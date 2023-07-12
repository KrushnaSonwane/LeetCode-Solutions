class Solution:
    def findBall(self, A: List[List[int]]) -> List[int]:
        m, n = len(A), len(A[0])
        res = [-1] * n
        @cache
        def dfs(r, c):
            if r == m: return c
            if r in [-1,m] or c in [-1,n]: return -1
            if A[r][c] == 1:
                if c+1 < n and A[r][c+1] == 1: return dfs(r+1,c+1)
            if A[r][c] == -1:
                if c-1 >= 0 and A[r][c-1] == -1: return dfs(r+1,c-1)
            return -1

        for i in range(n):
            res[i] = dfs(0, i)
        return res