class Solution:
    def modifiedMatrix(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        max_ = [0 for _ in range(n)]
        for j in range(n):
            mx = 0
            for i in range(m):
                mx = max(mx, A[i][j])
            max_[j] = mx
        for i in range(m):
            for j in range(n):
                if A[i][j] == -1:
                    A[i][j] = max_[j]
        return A