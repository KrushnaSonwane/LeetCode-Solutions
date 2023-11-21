class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        A, Q = {(0,0): 0}, [(0, 0, 0)]
        m, n = len(grid), len(grid[0])
        while Q:
            cost, i, j = heappop(Q)
            if i == m-1 and j == n-1: return cost
            for num, x, y in [[1, i, j+1], [2, i, j-1], [3, i+1, j], [4, i-1, j]]:
                if x in [-1, m] or y in [-1, n]: continue
                curr = 1 if grid[i][j] != num else 0
                if (x, y) in A and A[(x, y)] <= cost+curr: continue
                A[(x, y)] = cost+curr
                heappush(Q, [cost+curr, x, y])
        return res