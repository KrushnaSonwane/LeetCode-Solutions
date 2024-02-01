class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            if i == len(costs): return 0
            res = inf
            for k in range(len(costs[i])):
                if j == k: continue
                res = min(res, dfs(i+1, k) + costs[i][k])
            return res
        return dfs(0, -1)