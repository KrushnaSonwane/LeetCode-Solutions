class Solution:
    def candy(self, R: List[int]) -> int:
        A, B = [1 for _ in R], [1 for _ in R]
        for i in range(1, len(R)):
            if R[i] > R[i-1]:
                A[i] = A[i-1] + 1
        for i in range(len(R)-2, -1, -1):
            if R[i] > R[i+1]:
                B[i] = B[i+1] + 1
        return sum(max(a, b) for a, b in zip(A, B))