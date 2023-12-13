class Solution:
    def numSpecial(self, A: List[List[int]]) -> int:
        res, m, n = 0, len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    count = 0
                    for k in range(n):
                        count += A[i][k]
                    for k in range(m):
                        count += A[k][j]
                    res += count == 2
        return res