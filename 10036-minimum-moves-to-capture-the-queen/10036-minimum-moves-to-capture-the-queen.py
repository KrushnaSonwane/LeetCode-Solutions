class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        for i in range(a+1, 9):
            if (i, b) == (c, d):
                break
            if (i, b) == (e, f): return 1
        for i in range(a-1, 0, -1):
            if (i, b) == (c, d):
                break
            if (i, b) == (e, f): return 1
        for i in range(b+1, 9):
            if (a, i) == (c, d): break
            if (a, i) == (e, f): return 1
        for i in range(b-1, 0, -1):
            if (a, i) == (c, d): break
            if (a, i) == (e, f): return 1
        i, j = c-1, d-1
        while i >= 1 and j >= 1 and (i, j) != (a, b):
            if (i, j) == (e, f): return 1
            i -= 1
            j -= 1
        i, j = c+1, d+1
        while i <= 8 and j <= 8 and (i, j) != (a, b):
            if (i, j) == (e, f): return 1
            i += 1
            j += 1
        i, j = c-1, d+1
        while i >= 1 and j <= 8 and (i, j) != (a, b):
            if (i, j) == (e, f): return 1
            i -= 1
            j += 1
        i, j = c+1, d-1
        while i <= 8 and j >= 1 and (i, j) != (a, b):
            if (i, j) == (e, f): return 1
            i += 1
            j -= 1
        return 2