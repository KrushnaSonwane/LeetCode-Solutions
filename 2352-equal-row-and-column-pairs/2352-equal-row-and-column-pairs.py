class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res, n = 0, len(grid)
        hashT = defaultdict(int)
        for i in range(n):
            hashT['.'.join(str(grid[i][j]) for j in range(n))] += 1
        for i in range(n):
            res += hashT['.'.join(str(grid[j][i]) for j in range(n))]
        return res