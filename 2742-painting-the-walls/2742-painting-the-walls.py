class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n, dp = len(cost), {}
        def dfs(i, rem):
            if i == len(cost):
                return 0 if rem >= 0 else inf
            if (i, rem) in dp: return dp[(i, rem)]
            take = dfs(i + 1, min(n, rem + time[i])) + cost[i]
            notTake = dfs(i + 1, rem - 1)
            dp[(i, rem)] = min(take, notTake)
            return dp[(i, rem)]
        return dfs(0, 0)