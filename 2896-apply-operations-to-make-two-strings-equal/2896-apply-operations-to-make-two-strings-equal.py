class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        A = []
        for i, (a, b) in enumerate(zip(s1, s2)):
            if a != b:
                A.append(i)
        @cache
        def dfs(i, rem):
            if i == len(A):
                return inf if rem != 0 else 0
            res = inf
            if i+1 < len(A):
                res = dfs(i+2, rem) + (A[i+1] - A[i])
            if rem:
                res = min(res, dfs(i+1, rem-1)+x)
            res = min(res, dfs(i+1, rem+1))
            return res
        res = dfs(0, 0)
        return -1 if res == inf else res