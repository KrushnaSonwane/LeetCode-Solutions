class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        @cache
        def dfs(i, last):
            if i == len(days): return 0
            if days[i] < last:
                res = dfs(i+1, last)
            else:
                res = dfs(i+1, days[i]+1) + cost[0]
                res = min(res, dfs(i+1, days[i] + 7) + cost[1])
                res = min(res, dfs(i+1, days[i] + 30) + cost[2])
            return res
        return dfs(0, 0)