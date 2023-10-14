class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9+7
        @lru_cache(None)
        def dfs(i, last, count):
            if count > rollMax[last-1]: return 0
            if i == n: return 1
            return sum(dfs(i+1, num, 1 if num != last else count + 1) for num in range(1, 7)) % MOD
        return dfs(0, 0, 0)