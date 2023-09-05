class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        @lru_cache(None)
        def dfs(i, f, s, t):
            if i == len(num): return t
            res = False
            for j in range(i, len(num)):
                a = num[i: j+1]
                if f == -1 and a == str(int(a)):
                    res = res or dfs(j+1, int(num[i: j+1]), s, t)
                elif s == -1 and a == str(int(a)):
                    res = res or dfs(j+1, f, int(num[i: j+1]), t)
                else:
                    if int(a) == f + s and a == str(int(a)):
                        res = res or dfs(j+1, s, int(a), True)
            return res
        return dfs(0, -1, -1, False)