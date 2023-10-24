class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        @cache
        def dfs(i, rem, n):
            if rem == 0: return 0
            if i >= n: return 0
            res = dfs(i+1, rem, n)
            res = max(res, dfs(i+2, rem-1, n) + slices[i])
            return res
        n = len(slices) // 3
        res = dfs(1, n, len(slices))
        slices.pop()
        return max(res, dfs(0, n, len(slices)))