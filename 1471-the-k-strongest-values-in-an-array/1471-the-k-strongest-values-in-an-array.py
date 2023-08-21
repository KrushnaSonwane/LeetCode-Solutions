class Solution:
    def getStrongest(self, A: List[int], k: int) -> List[int]:
        A.sort()
        res, m = [], A[(len(A)-1)//2]
        l, r = 0, len(A)-1
        for _ in range(k):
            ll, rr = abs(A[l] - m), abs(A[r]-m)
            res.append(A[l] if ll > rr else A[r])
            if ll > rr:
                l += 1
            else:
                r -= 1
        return res