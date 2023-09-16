class Solution:
    def minimumEffortPath(self, A: List[List[int]]) -> int:
        def solve(m):
            Q, visit = [(0, 0, A[0][0])], {(0,0)}
            while Q:
                i, j, last = Q.pop(0)
                if (i,j)==(len(A)-1,len(A[0])-1): return 1
                for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if x in [-1, len(A)] or y in [-1, len(A[0])] or (x, y) in visit or abs(A[x][y]-last) > m: continue
                    visit.add((x,y))
                    Q.append((x,y,A[x][y]))
            return False
        l, r = 0, 10**6
        while l < r:
            m = (l+r) // 2
            if solve(m):
                r = m
            else:
                l = m + 1
        return l