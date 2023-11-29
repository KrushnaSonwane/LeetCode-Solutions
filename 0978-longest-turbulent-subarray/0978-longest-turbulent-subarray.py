class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        res, count, last = 1, 1, A[0]
        for i in range(1, len(A)):
            if i % 2 and last > A[i]:
                count += 1
            elif i % 2 == 0 and last < A[i]:
                count += 1
            else:
                count = 1
            res = max(res, count)
            last = A[i]
        count, last = 1, A[0]
        for i in range(1, len(A)):
            if i % 2 and last < A[i]:
                count += 1
            elif i % 2 == 0 and last > A[i]:
                count += 1
            else:
                count = 1
            res = max(res, count)
            last = A[i]
        return res