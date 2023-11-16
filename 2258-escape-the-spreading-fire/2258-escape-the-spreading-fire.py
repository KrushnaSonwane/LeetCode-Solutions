class Solution:
    def maximumMinutes(self, A: List[List[int]]) -> int:
        m, n, visit = len(A), len(A[0]), set()
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        Q = []
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    Q.append([1, i, j])
                if A[i][j] > 0:
                    visit.add((i, j))
                    dp[i][j] = 0
        while Q:
            cost, i, j = Q.pop(0)
            for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if x in [-1, m] or y in [-1, n]: continue
                if (x, y) in visit: continue
                dp[x][y] = cost
                Q.append((cost+1, x, y))
                visit.add((x, y))
        def isValid(t):
            Q = [[t, 0, 0]]
            okay = set({(0, 0)})
            while Q:
                time, i, j = Q.pop(0)
                if (i, j) == (m-1, n-1): return True
                for x, y in [(i+1,j), (i-1, j), (i,j-1), (i,j+1)]:
                    if x in [-1, m] or y in [-1, n] or (x, y) in okay: continue
                    if dp[x][y] != -1 and (x, y) == (m-1, n-1) and dp[x][y] >= time+1:
                        return True
                    if dp[x][y] != -1 and dp[x][y] <= time+1: continue
                    okay.add((x, y))
                    Q.append((time+1, x, y))
            return False
        
        l, r = 0, 10**9
        res = -1
        while r >= l:
            mid = (r + l) // 2
            if isValid(mid):
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        return res