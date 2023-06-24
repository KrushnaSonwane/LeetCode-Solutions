class Solution:
    def maxArea(self, A: List[int]) -> int:
        res = 0
        l, r = 0, len(A) - 1
        while r > l:
            res = max(res, min(A[l], A[r]) * (r - l))
            if A[r] > A[l]: l += 1
            else: r -= 1
        return res