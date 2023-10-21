class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @cache
        def dfs(i, start, tight, mask):
            if i == len(s): return start
            res = 0
            if not start:
                res = dfs(i+1, 0, False, mask)
            A = [ch for ch in mask]
            for num in range(10):
                if start == num == 0 or mask[num] == '1': continue
                if tight and num > int(s[i]): continue
                A[num] = '1'
                res += dfs(i+1, 1, tight and num == int(s[i]), ''.join(A))
                A[num] = '0'
            return res
        return dfs(0, 0, True, '0'*10)