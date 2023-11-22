class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dist, n = {(0,0): grid[0][0]}, len(grid)
        Q = [(grid[0][0], 0, 0)]
        while Q:
            cost, i, j = heappop(Q)
            if (i, j) == (n-1, n-1): return cost
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x in [-1, n] or y in [-1, n]: continue
                curr = max(cost, grid[x][y])
                if (x, y) in dist and dist[(x, y)] <= curr: continue
                dist[(x, y)] = curr
                heappush(Q, (curr, x, y))
        return -1