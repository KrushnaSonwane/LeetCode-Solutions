class Solution:
    def maximumSafenessFactor(self, A: List[List[int]]) -> int:
        def isValid(key):
            if A[0][0] >= key:
                Q = [(0, 0)]
                visit = {(0,0)}
                while Q:
                    i, j = Q.pop(0)
                    if (i,j)==(n-1,n-1): return 1
                    for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if x in [-1, n] or y in [-1, n] or (x, y) in visit or key > A[x][y]: continue
                        Q.append((x,y))
                        visit.add((x,y))
            return 0

        n, visit, Q = len(A), set(), []
        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    visit.add((i, j))
                    Q.append((i, j))
        count = 0
        while Q:
            for _ in range(len(Q)):
                i, j = Q.pop(0)
                A[i][j] = count
                for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if x in [-1, n] or y in [-1, n] or (x, y) in visit: continue
                    Q.append((x, y))
                    visit.add((x, y))
            count += 1
        l, r = 0, n
        res = 0
        while r >= l:
            mid = (r+l)//2
            if isValid(mid):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res