class Solution:
    def putMarbles(self, W: List[int], k: int) -> int:
        A = [W[i] + W[i+1] for i in range(len(W) - 1)]
        A.sort()
        return sum(A[-1:-k:-1]) - sum(A[:k-1])