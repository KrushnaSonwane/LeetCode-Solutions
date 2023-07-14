class Solution:
    def minCost(self, A: List[int], B: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        res = 0
        if A[0] > B[0]:
            res += sum(rowCosts[B[0]:A[0]])
        else:
            res += sum(rowCosts[A[0]+1: B[0]+1])
        if A[1] > B[1]:
            res += sum(colCosts[B[1]:A[1]])
        else:
            res += sum(colCosts[A[1]+1: B[1]+1])
        return res