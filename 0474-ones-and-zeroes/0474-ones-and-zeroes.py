class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dfs(i, x, y):
            if i == len(strs): return 0
            res = dfs(i + 1, x, y)
            a, b = strs[i].count('0'), strs[i].count("1")
            if x >= a and y >= b:
                res = max(res, dfs(i + 1, x - a, y - b) + 1)
            return res
        return dfs(0, m, n)