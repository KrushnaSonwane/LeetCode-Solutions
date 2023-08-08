class Solution:
    def nextPermutation(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(A)-2
        while i >= 0 and A[i] >= A[i+1]:
            i-=1
        if i >= 0:
            j = len(A)-1
            while A[j] <= A[i]:
                j -= 1
            A[i], A[j] = A[j], A[i]
        l, r = i+1, len(A)-1
        while r > l:
            A[l], A[r] = A[r], A[l]
            l += 1
            r -= 1