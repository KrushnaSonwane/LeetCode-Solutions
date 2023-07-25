class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        while r > l:
            m = (r+l)//2
            if A[m]>A[m+1] and A[m]>A[m-1]: return m
            elif A[m]>A[m+1] and A[m-1]>A[m]: r = m-1
            else: l = m + 1
        return l