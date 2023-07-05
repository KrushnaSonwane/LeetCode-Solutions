class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        res, O, Z = 0, 0, 0
        p = 0
        for i, a in enumerate(A):
            if a: O += 1
            else: Z += 1
            while Z > 1:
                if A[p]: O -= 1
                else: Z -= 1
                p += 1
            res = max(res, O if Z else O - 1)
        return res