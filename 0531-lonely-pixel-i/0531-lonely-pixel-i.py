class Solution:
    def findLonelyPixel(self, A: List[List[str]]) -> int:
        rows, cols = Counter(), Counter()
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1
        res = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 'B' and rows[i] == 1 and cols[j] == 1:
                    res += 1
        return res