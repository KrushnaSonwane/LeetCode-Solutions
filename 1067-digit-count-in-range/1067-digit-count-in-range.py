class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        @cache
        def dfs(i, start, tight, count, s):
            if i == len(s):
                return count
            res = 0
            if not start:
                res = dfs(i+1, 0, 0, count, s)
            for num in range(10):
                if not start and num == 0: continue
                if tight and int(s[i]) < num: break
                if num == d:
                    count += 1
                res += dfs(i+1, 1, tight and s[i] == str(num), count, s)
                if num == d:
                    count -= 1
            return res
        return dfs(0, 0, 1, 0, str(high)) - dfs(0, 0, 1, 0, str(low-1))