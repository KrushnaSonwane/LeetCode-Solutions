class Solution:
    def largest1BorderedSquare(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        AA = [[0 for _ in range(n)] for _ in range(m)]
        BB = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            last = 0
            for j in range(n):
                if A[i][j]: last += 1
                else: last = 0
                AA[i][j] = last
        for i in range(n):
            last = 0
            for j in range(m):
                if A[j][i]: last += 1
                else: last = 0
                BB[j][i] = last
        res = 0
        for i in range(m):
            for j in range(n):
                for c in range(AA[i][j]):
                    ii, jj = i + c, j - c
                    if ii < m and jj >= 0:
                        if c+1 <= AA[ii][j] and c + 1 <= BB[ii][jj] and BB[ii][j] >= c + 1:
                            res = max(res, (c+1) ** 2)
        return res