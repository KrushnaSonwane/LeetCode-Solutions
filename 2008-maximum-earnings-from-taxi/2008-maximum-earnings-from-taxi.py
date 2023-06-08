class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        @cache
        def dfs(i):
            if i >= len(rides): return 0
            unTake = dfs(i + 1)
            take = (rides[i][1] - rides[i][0]) + rides[i][2]
            l, r = i, len(rides) - 1
            res = -1
            while r >= l:
                mid = (r + l) // 2
                if rides[mid][0] >= rides[i][1]:
                    res = mid if res == -1 else min(mid, res)
                    r = mid - 1
                else:
                    l = mid + 1
            take = take + (dfs(res) if res != -1 else 0)
            return max(unTake, take)
        return dfs(0)