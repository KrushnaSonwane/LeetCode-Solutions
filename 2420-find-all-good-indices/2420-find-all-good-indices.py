class Solution:
    def goodIndices(self, A: List[int], k: int) -> List[int]:
        l, r = 0, 0
        if k == 1: return [i for i in range(1, len(A)-1)]
        res = []
        for i in range(4, min(k+k, len(A))):
            if A[i-1] <= A[i]: r += 1
            else: r = 0
        for i in range(2, len(A)-k):
            if A[i-2] >= A[i-1]: l += 1
            else: l = 0
            if A[i+k] >= A[i+k-1]: r += 1
            else: r = 0
            if l >= k-1 and r >= k-1: res.append(i)
        return res 