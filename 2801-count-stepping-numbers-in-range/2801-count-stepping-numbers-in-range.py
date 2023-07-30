class Solution:
    def f(self, num):
        @cache
        def dfs(i, last, tight, start):
            if i == len(num): return 1
            res = 0
            if not start:
                res += dfs(i+1, last, tight, start)
                for d in range(1, 10):
                    res += dfs(i+1, d, tight, True)
            else:
                if tight:
                    if last+1<=int(num[i]):
                        res += dfs(i+1, last+1, int(num[i])==last+1, start)
                    if last-1>=0 and int(num[i]) >= last-1:
                        res += dfs(i+1, last-1, int(num[i])==last-1, start)
                else:
                    if last+1<=9:
                        res += dfs(i+1, last+1, tight, start)
                    if last-1>=0:
                        res += dfs(i+1, last-1, tight, start)
            return res
        ans = 0
        for i in range(int(num[0])+1):
            if i == 0:
                ans += dfs(1, -1, False, False)
            else:
                ans += dfs(1, i, int(num[0])==i, True)
        return ans
        
    def countSteppingNumbers(self, low: str, high: str) -> int:
        a, b = self.f(high), self.f(str(int(low)-1))
        res = (a-b) % (10**9+7)
        return res