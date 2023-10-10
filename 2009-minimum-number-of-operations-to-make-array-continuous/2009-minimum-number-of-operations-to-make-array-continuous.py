class Solution:
    def minOperations(self, A: List[int]) -> int:
        A.sort()
        l, r, res = 0, 0, inf
        hashT = defaultdict(int)
        count = 0
        while r < len(A):
            hashT[A[r]] += 1
            count += hashT[A[r]] > 1
            while A[r] - A[l] > len(A)-1:
                count -= hashT[A[l]] > 1
                hashT[A[l]] -= 1
                l += 1
            res = min(res, (len(A) - (r - l + 1)) + count)
            r += 1
        return res