class Solution:
    def minProductSum(self, A: List[int], B: List[int]) -> int:
        A.sort()
        B.sort(reverse = True)
        res = 0
        for a, b in zip(A, B):
            res += a * b
        return res