class Solution:
    def maxKilledEnemies(self, A: List[List[str]]) -> int:
        m, n = len(A), len(A[0])
        left, right = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
        up, down = [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
        for i in range(m):
            sum_ = 0
            for j in range(n):
                if A[i][j] == 'W':
                    sum_ = 0
                elif A[i][j] == 'E':
                    sum_ += 1
                left[i][j] = sum_
        for i in range(m):
            sum_ = 0
            for j in range(n-1, -1, -1):
                if A[i][j] == 'W':
                    sum_ = 0
                elif A[i][j] == 'E':
                    sum_ += 1
                right[i][j] = sum_
        for j in range(n):
            sum_ = 0
            for i in range(m):
                if A[i][j] == 'W':
                    sum_ = 0
                elif A[i][j] == 'E':
                    sum_ += 1
                down[i][j] = sum_
        for j in range(n):
            sum_ = 0
            for i in range(m-1, -1, -1):
                if A[i][j] == 'W':
                    sum_ = 0
                elif A[i][j] == 'E':
                    sum_ += 1
                up[i][j] = sum_
        res = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == '0':
                    res = max(res, left[i][j] + right[i][j] + up[i][j] + down[i][j])
        return res