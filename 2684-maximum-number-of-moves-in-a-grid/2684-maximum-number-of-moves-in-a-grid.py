class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n - 2, -1, -1):
            for i in range(m):
                curr = []
                if i > 0 and grid[i][j] < grid[i - 1][j + 1]: curr.append(cache[i - 1][j + 1])
                if grid[i][j] < grid[i][j + 1]: curr.append(cache[i][j + 1])
                if i < m - 1 and grid[i][j] < grid[i + 1][j + 1]: curr.append(cache[i + 1][j + 1])
                cache[i][j] = max(curr) + 1 if curr else 0
        return max(cache[i][0] for i in range(m))