class Solution:
    def checkXMatrix(self, A: List[List[int]]) -> bool:
        n = len(A)
        sum_ = sum(A[i][j] for i in range(n) for j in range(n))
        j = 0;k = n - 1
        for i in range(n):
            if A[i][j] <= 0: return 0
            if A[i][k] <= 0: return 0
            sum_ -= A[i][k] + A[i][j] if k != j else A[i][k]
            j += 1; k-= 1
        return 1 if sum_ == 0 else 0