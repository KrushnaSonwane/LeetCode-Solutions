class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        n = str(n)
        @cache
        def dfs(i, s, t, mask, d):
            if i == len(n):
                return 1 if d else 0
            res = 0
            if not s:
                res = dfs(i+1, s, False, mask, d)
            for digit in range(10):
                if (i == 0 or not s) and digit == 0: continue
                if t and digit > int(n[i]): break
                A = [ch for ch in mask]
                B = A.copy()
                B[digit] = '1'
                res += dfs(i+1, 1, t and digit == int(n[i]), ''.join(B), d or A[digit]=='1')
            return res
        return dfs(0, 0, True, '0'*10, False)