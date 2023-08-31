class Solution:
    def minTimeToVisitAllPoints(self, A: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(A)):
            x, y = abs(A[i][0]-A[i-1][0]), abs(A[i][1]-A[i-1][1])
            if y > x:
                x, y = y, x
            res += y + x - y
        return res