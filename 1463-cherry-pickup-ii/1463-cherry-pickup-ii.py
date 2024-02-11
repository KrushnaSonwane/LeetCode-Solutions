class Solution:
    def cherryPickup(self, A: List[List[int]]) -> int:
        @cache
        def dfs(i, j, k):
            if i == len(A):
                return 0
            res = 0
            for jj in [j-1, j, j+1]:
                for kk in [k-1, k, k+1]:
                    if 0 <= jj < len(A[0]) and 0 <= kk < len(A[0]):
                        a, b = A[i][j], A[i][k]
                        if j == k:
                            res = max(res, dfs(i+1, jj, kk) + a)
                        else:
                            res = max(res, dfs(i+1, jj, kk) + a + b)
            return res
        return dfs(0, 0, len(A[0])-1)
                        