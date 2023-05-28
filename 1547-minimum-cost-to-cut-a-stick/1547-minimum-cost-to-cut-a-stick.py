class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        dp = {}
        def dfs(i, j):
            if j <= i: return 0
            if (i, j) in dp: return dp[(i, j)]
            res = float("inf")
            for k in range(len(cuts)):
                if cuts[k] <= i: continue
                if cuts[k] >= j: continue
                temp = j - i + dfs(i, cuts[k]) + dfs(cuts[k], j)
                res = min(res, temp)
            dp[(i, j)] = res if res != float("inf") else 0
            return dp[(i, j)]
        return dfs(0, n)