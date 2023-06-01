class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]: return -1
        queue = [[1, 0, 0]]
        while queue:
            cost, r, c= heapq.heappop(queue)
            if r == n - 1 and c == n - 1: return cost
            for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1), (r + 1, c + 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1)]:
                if x in [-1, n] or y in [-1, n] or grid[x][y]: continue
                heapq.heappush(queue, [cost + 1, x, y])
                grid[x][y] = 1
        return -1