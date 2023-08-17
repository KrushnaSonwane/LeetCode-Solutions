class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        visit, Q = set(), []
        for i in range(m):
            for j in range(n):
                if (i, j) not in visit and mat[i][j]==0:
                    for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                        if x in [-1, m] or y in [-1, n] or (x, y) in visit or mat[x][y]==0: continue
                        Q.append((x,y))
                        visit.add((x,y))
        res = 1
        while Q:
            for _ in range(len(Q)):
                i, j = Q.pop(0)
                mat[i][j] = res
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if x in [-1, m] or y in [-1, n] or (x, y) in visit or mat[x][y]==0: continue
                    Q.append((x,y))
                    visit.add((x,y))
            res += 1
        return mat