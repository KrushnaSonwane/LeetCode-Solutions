class Solution:
    def solve(self, num, min_, max_):
        @cache
        def dfs(i, tight, start, sum_):
            if sum_ > max_: return 0
            if i == len(num):
                return 1 if min_ <= sum_ <=max_ else 0
            res = 0
            if not start:
                res += dfs(i+1, tight, start, sum_)
                for d in range(1, 10):
                    res += dfs(i+1, tight, True, sum_+d)
            else:
                if not tight:
                    for d in range(0, 10):
                        res += dfs(i+1, tight, True, sum_+d)
                else:
                    for d in range(0, int(num[i])+1):
                        res += dfs(i+1, num[i]==str(d), True, sum_+d)
            return res
        ans = 0
        for i in range(int(num[0])+1):
            ans += dfs(1, i==int(num[0]), i >= 1, i)
        return ans
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        res = self.solve(num2, min_sum, max_sum)-self.solve(str(int(num1)-1), min_sum, max_sum)
        return res % MOD