class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9+7
        @cache
        def dfs(i, count):
            if i == goal:
                return 1 if count == n else 0
            res = dfs(i+1, count+1) * max(n-count, 0)
            res += dfs(i+1, count) * max(0, count-k)
            res %= mod
            return res
        return dfs(0, 0) 