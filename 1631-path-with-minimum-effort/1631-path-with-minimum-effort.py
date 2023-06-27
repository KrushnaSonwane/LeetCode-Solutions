class Solution:
    def isValid(self, d, A):
        m, n = len(A), len(A[0])
        visit = {(0, 0)}
        Q = [(0, 0)]
        while Q:
            for _ in range(len(Q)):
                i, j = Q.pop(0)
                if (i, j) == (m-1, n-1): return 1
                for r, c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if r in [-1,m] or c in [-1,n] or (r,c) in visit or abs(A[i][j]-A[r][c])>d: continue
                    visit.add((r, c))
                    Q.append((r, c))
        return 0

    def minimumEffortPath(self, A: List[List[int]]) -> int:
        l, r = 0, 10**6
        while r > l:
            mid = (r + l) // 2
            if self.isValid(mid, A): r = mid
            else: l = mid + 1
        return l