class Solution:
    def numRookCaptures(self, A: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if A[i][j] == 'R': r, c = i, j
        res = 0
        for i in range(r, -1, -1):
            if A[i][c] == 'B': break
            if A[i][c] == 'p':
                res += 1
                break
        for i in range(r, 8):
            if A[i][c] == 'B': break
            if A[i][c] == 'p':
                res += 1
                break
        for i in range(c, -1, -1):
            if A[r][i] == 'B': break
            if A[r][i] == 'p': 
                res += 1
                break
        for i in range(c, 8):
            if A[r][i] == 'B': break
            if A[r][i] == 'p':
                res += 1
                break
        return res