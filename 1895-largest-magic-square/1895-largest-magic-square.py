class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        colSum = [[0 for _ in range(n)] for _ in range(m)]
        rowSum = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            sum_ = 0
            for j in range(n):
                sum_ += grid[i][j]
                colSum[i][j] = sum_
        for i in range(n):
            sum_ = 0
            for j in range(m):
                sum_ += grid[j][i]
                rowSum[j][i] = sum_
        ans = 1
        for i in range(m):
            for j in range(n):
                res = ans
                while i + res+1 <= m and j + res +1<= n:
                    visit = set()
                    for k in range(i, i + res+1):
                        if j == 0: visit.add(colSum[k][j+res])
                        else: visit.add(colSum[k][j+res]-colSum[k][j-1])
                    for k in range(j, j+res+1):
                        if i==0: visit.add(rowSum[i+res][k])
                        else: visit.add(rowSum[i+res][k]-rowSum[i-1][k])
                    visit.add(sum(grid[i+k][j+k] for k in range(res+1)))
                    visit.add((sum(grid[i+res-k][j+k] for k in range(res+1))))
                    res += 1
                    if len(visit)==1: ans = max(ans, res)
        return ans