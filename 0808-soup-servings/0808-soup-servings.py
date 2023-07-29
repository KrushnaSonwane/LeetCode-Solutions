class Solution:
    def soupServings(self, N: int) -> float:
        if N > 4800: return 1
        @cache
        def dfs(a, b):
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1
            if b <= 0: return 0
            return 0.25 * (dfs(a - 4, b) + dfs(a - 3, b - 1) + dfs(a - 2, b - 2) + dfs(a - 1, b - 3))
        N = math.ceil(N / 25.0)
        return dfs(N, N)