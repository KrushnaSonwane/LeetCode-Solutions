class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n, hashT = len(grid), defaultdict(int)
        for i in range(n):
            hashT['.'.join(str(grid[i][j]) for j in range(n))] += 1
        return sum(hashT['.'.join(str(grid[j][i]) for j in range(n))] for i in range(n))