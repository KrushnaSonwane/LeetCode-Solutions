class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        hashT = {}
        for i, number in enumerate(strs):
            hashT[i] = [0, 0]
            for ch in number:
                if ch == '0': hashT[i][0] += 1
                else: hashT[i][1] += 1
        @cache
        def dfs(i, x, y):
            if i == len(strs): return 0
            res = dfs(i + 1, x, y)
            if x >= hashT[i][0] and y >= hashT[i][1]:
                res = max(res, dfs(i + 1, x - hashT[i][0], y - hashT[i][1]) + 1)
            return res
        return dfs(0, m, n)