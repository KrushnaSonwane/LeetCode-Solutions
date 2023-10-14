class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @lru_cache(None)
        def dfs(i, rem):
            if i == n:
                return 0 if rem >= 0 else inf
            take = dfs(i + 1, min(n, rem + time[i])) + cost[i]
            notTake = dfs(i + 1, rem - 1)
            return min(take, notTake)
        return dfs(0, 0)