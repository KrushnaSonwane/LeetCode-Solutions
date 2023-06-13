class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res, n = 0, len(grid)
        hashT = defaultdict(int)
        for i in range(n):
            s = ''
            for j in range(n):
                s += str(grid[i][j]) + '.'
            hashT[s] += 1
        for i in range(n):
            s = ''
            for j in range(n):
                s += str(grid[j][i]) + '.'
            res += hashT[s]
        return res