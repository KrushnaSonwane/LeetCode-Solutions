class Solution:
    def maxHeight(self, A: List[List[int]]) -> int:
        for a in A:
            a.sort()
        A.sort()
        @cache
        def dfs(i, j):
            if i == len(A):
                return 0
            res = dfs(i+1, j)
            if j == -1:
                a, b, c = -inf, -inf, -inf
            else:
                a, b, c = A[j]
            x, y, z = A[i]
            if x >= a and y >= b and z >= c:
                res = max(res, dfs(i+1, i) + z)
            return res
        return dfs(0, -1)