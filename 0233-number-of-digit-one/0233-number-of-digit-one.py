class Solution:
    def countDigitOne(self, n: int) -> int:
        A = str(n)
        @cache
        def dfs(i, s, t, c):
            if i == len(A):
                return c
            res = 0
            if not s:
                res += dfs(i+1, s, False, 0)
            for d in range(10):
                if (i == 0 or not s) and d == 0: continue
                if t and d > int(A[i]): break
                res += dfs(i+1, 1, t and d == int(A[i]), c + (1 if d == 1 else 0))
            return res
        return dfs(0, 0, True, 0)