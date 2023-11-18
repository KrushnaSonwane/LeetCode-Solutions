class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visit, Q = {(0, 0, k)}, [[0, 0, 0, k]]
        m, n = len(grid), len(grid[0])
        while Q:
            step, i, j, rem = heappop(Q)
            if (i, j) == (m-1, n-1): return step
            for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if x in [-1, m] or y in [-1, n] or (x, y, rem) in visit: continue
                visit.add((x,y,rem))
                if grid[x][y] == 0:
                    heappush(Q, [step+1, x, y, rem])
                elif rem:
                    heappush(Q, [step+1, x, y, rem-1])
        return -1