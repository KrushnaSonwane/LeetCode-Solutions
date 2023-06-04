class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        res = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                size = 0
                while i - size >= 0 and i + size < m and j - size >= 0 and j + size < n:
                    if not size: res.append(grid[i][j])
                    else:
                        temp = j
                        sum_ = 0
                        for k in range(i - size, i):
                            sum_ += grid[k][temp]
                            temp -= 1
                        temp = i
                        for k in range(j - size, j):
                            sum_ += grid[temp][k]
                            temp += 1
                        temp = j
                        for k in range(i + size, i, -1):
                            sum_ += grid[k][temp]
                            temp += 1
                        temp = i
                        for k in range(j + size, j, -1):
                            sum_ += grid[temp][k]
                            temp -= 1
                        res.append(sum_)
                    size += 1
        res.sort()
        arr = set()
        while res and len(arr) != 3:
            arr.add(res.pop())
        return sorted(list(arr))[::-1]