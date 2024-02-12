class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:
        m, n = len(A), len(A[0])
        AA = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] == '1':
                    res = inf
                    if i - 1 >= 0:
                        res = min(res, AA[i-1][j])
                    else:
                        res = 0
                    if j - 1 >= 0:
                        res = min(res, AA[i][j-1])
                    else:
                        res = 0
                    if j - 1 >= 0 and i - 1 >= 0:
                        res = min(res, AA[i-1][j-1])
                    else:
                        res = 0
                    AA[i][j] = res + 1
        return max(max(a) * max(a) for a in AA)