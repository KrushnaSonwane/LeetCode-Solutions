class Solution:
    def containsCycle(self, A: List[List[str]]) -> bool:
        m, n = len(A), len(A[0])
        visit = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visit:
                    Q = [(i,j,inf,inf)]
                    visit.add((i,j))
                    while Q:
                        r, c, t1, t2 = Q.pop(0)
                        for x, y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                            if x in [-1, m] or y in [-1,n] or (x,y)==(t1,t2) or A[x][y]!=A[i][j]: continue
                            if (x, y) in visit: return 1
                            Q.append((x,y,r,c))
                            visit.add((x,y))
        return 0