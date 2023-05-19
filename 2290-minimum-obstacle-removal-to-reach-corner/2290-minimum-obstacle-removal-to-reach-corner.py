class Solution(object):
    def minimumObstacles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = [[0, 0, 0]]
        heapq.heapify(queue)
        dist, m, n = {(0, 0): 0}, len(grid), len(grid[0])
        def dfs(r, c, cost):
            if r in [-1, m] or c in [-1, n] or ((r, c) in dist and dist[(r, c)] <= cost):
                return
            dist[(r, c)] = cost
            heapq.heappush(queue, [cost + grid[r][c], r, c])
        
        while queue:
            cost, r, c = heapq.heappop(queue)
            if r == m - 1 and c == n - 1: return cost
            dfs(r - 1, c, cost)
            dfs(r + 1, c, cost)
            dfs(r, c - 1, cost)
            dfs(r, c + 1, cost)