class Solution:
    def getWinner(self, A: List[int], k: int) -> int:
        count = 0
        for i in range(1, len(A)):
            if A[i] > A[0]:
                A[0], count = A[i], 0
            count += 1
            if count == k: return A[0]
        return A[0]