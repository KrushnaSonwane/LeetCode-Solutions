class Solution:
    def maxSum(self, A: List[int], B: List[int]) -> int:
        res, mod = 0, 10**9+7
        i, j = 0, 0
        a, b = 0, 0
        while i < len(A) or j < len(B):
            if len(A)>i:
                a += A[i]
                while j < len(B) and A[i] > B[j]:
                    b += B[j]
                    j += 1
                if j < len(B) and A[i]==B[j]:
                    b += B[j]
                    res += max(a, b)
                    a, b = 0, 0
                    j += 1
                i += 1
            else:
                while j < len(B):
                    b += B[j]
                    j += 1
        res += max(a, b)
        return res % mod