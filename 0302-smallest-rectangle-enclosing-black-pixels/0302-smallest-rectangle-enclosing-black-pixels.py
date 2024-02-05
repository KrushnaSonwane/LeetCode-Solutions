class Solution:
    def minArea(self, A: List[List[str]], x: int, y: int) -> int:
        minI, maxI, minJ, maxJ = x, x, y, y
        visit, Q = set({(x, y)}), [(x, y)]
        while Q:
            i, j = Q.pop(0)
            minI, maxI = min(minI, i), max(maxI, i)
            minJ, maxJ = min(minJ, j), max(maxJ, j)
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < len(A) and 0 <= y < len(A[0]) and (x, y) not in visit and A[x][y] == '1':
                    visit.add((x, y))
                    Q.append((x, y))
        x, y = maxI-minI+1, maxJ-minJ+1
        return x * y