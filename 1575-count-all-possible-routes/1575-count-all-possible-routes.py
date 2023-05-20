class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        dp = [[-1 for _ in range(fuel + 1)] for _ in locations]
        def dfs(i, f):
            if 0 > f: return 0
            if dp[i][f] != -1: return dp[i][f]
            count = 1 if i == finish else 0
            for j in range(len(locations)):
                if i == j: continue
                diff = abs(locations[i] - locations[j])
                if diff <= f:
                    count += dfs(j, f - diff)
            dp[i][f] = count
            return count
        return dfs(start, fuel) % (10**9 + 7)