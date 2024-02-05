class Solution:
    def minArea(self, A: List[List[str]], x: int, y: int) -> int:
        minI, maxI, minJ, maxJ = x, x, y, y
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == '1':
                    minI, maxI = min(minI, i), max(maxI,i)
                    minJ, maxJ = min(minJ, j), max(maxJ, j)
        x, y = maxI-minI+1, maxJ-minJ+1
        return x * y