class Solution:
    def tupleSameProduct(self, A: List[int]) -> int:
        hashT, res = defaultdict(int), 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                res += 8 * hashT[A[i]*A[j]]
                hashT[A[i]*A[j]] += 1
        return res