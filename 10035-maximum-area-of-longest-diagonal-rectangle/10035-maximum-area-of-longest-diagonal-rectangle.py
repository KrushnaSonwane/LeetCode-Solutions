class Solution:
    def areaOfMaxDiagonal(self, A: List[List[int]]) -> int:
        res = []
        for x, y in A:
            curr = sqrt(x*x + y*y)
            res.append([curr, x*y])
        res.sort()
        return res[-1][-1]