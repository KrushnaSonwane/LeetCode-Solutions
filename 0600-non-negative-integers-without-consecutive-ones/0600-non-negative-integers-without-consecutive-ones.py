class Solution:
    def findIntegers(self, n: int) -> int:
        s = ''
        while n:
            s = str(n%2) + s
            n //= 2
        @cache
        def dfs(i, start, tight, last):
            if i == len(s): return 1
            res = 0
            if not start:
                res = dfs(i+1, 0, False, 0)
            for num in [0, 1]:
                if start == num == 0: continue
                if tight and num > int(s[i]): continue
                if last == num == 1: continue
                res += dfs(i+1, 1, tight and int(s[i]) == num, num)
            return res
        return dfs(0, 0, True, 0)