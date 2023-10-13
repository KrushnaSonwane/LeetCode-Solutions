class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = sum(mat[r][c] for r in range(max(i - k, 0), min(m, i + k + 1)) for c in range(max(0, j - k), min(n, j+k+1)))
        return res