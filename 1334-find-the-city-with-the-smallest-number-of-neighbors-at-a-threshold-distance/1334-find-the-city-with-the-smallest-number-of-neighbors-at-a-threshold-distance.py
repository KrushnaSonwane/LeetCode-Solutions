class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], cost: int) -> int:
        A = [[inf for _ in range(n)] for _ in range(n)]
        for i in range(n):
            A[i][i] = 0
        for i, j, w in edges:
            A[i][j] = w
            A[j][i] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
        res, count = 0, inf
        for i in range(n):
            curr = sum(1 for j in range(n) if cost >= A[i][j])
            if curr <= count:
                res, count = i, curr
        return res