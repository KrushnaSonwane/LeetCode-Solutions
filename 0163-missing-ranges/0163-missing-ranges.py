class Solution:
    def findMissingRanges(self, A: List[int], lower: int, upper: int) -> List[List[int]]:
        A.sort()
        while A and A[0] < lower:
            A.pop(0)
        while A and A[-1] > upper:
            A.pop()
        res = []
        if len(A) == 0: return [[lower, upper]]
        if A[0] != lower:
            res.append([lower, A[0]-1])
        for i in range(1, len(A)):
            if A[i] - A[i-1] != 1:
                res.append([A[i-1]+1, A[i]-1])
        if A[-1] != upper:
            res.append([A[-1]+1, upper])
        return res