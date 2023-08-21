class Solution:
    def rotateGrid(self, A: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(A), len(A[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]
        top, bottom, right, left = 0, m-1, n-1, 0
        while right > left and bottom > top:
            t = []
            for i in range(left, right + 1):
                t.append([top, i])
            top += 1
            for i in range(top, bottom + 1):
                t.append([i, right])
            right -= 1
            for i in range(right, left - 1, -1):
                t.append([bottom,i])
            bottom -= 1
            for i in range(bottom, top-1, -1):
                t.append([i,left])
            left += 1
            curr = k % len(t)
            for i, j in t:
                if curr == len(t):
                    curr = 0
                x, y = t[curr]
                res[i][j] = A[x][y]
                curr += 1
        return res
        