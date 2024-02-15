class Solution:
    def missingElement(self, A: List[int], k: int) -> int:
        l, r = 0, len(A)-1
        a = 0
        while r >= l:
            mid = (r + l) // 2
            count = (A[mid]-A[0])-mid
            if count >= k:
                a = mid
                r = mid - 1
            else:
                l = mid + 1
        if a == 0:
            count = (A[-1]-A[0])-(len(A)-1)
            num = A[-1]
            res = k - count
        else:
            count = (A[a-1]-A[0])-(a-1)
            num = A[a-1]
            res = k-count
        return num + res