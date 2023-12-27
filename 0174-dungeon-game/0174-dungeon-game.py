class Solution:
    def calculateMinimumHP(self, A: List[List[int]]) -> int:

        def isValid(mid):
            m, n = len(A), len(A[0])
            dist = {}
            Q = [(mid+A[0][0], 0, 0)]
            while Q:
                cost, i, j = heappop(Q)
                if cost <= 0: continue
                if (i, j) == (m-1, n-1): return True
                for x, y in [(i+1, j), (i, j+1)]:
                    if x == m or y == n: continue
                    if (x, y) in dist and dist[(x, y)] >= cost + A[x][y]: continue
                    dist[(x, y)] = cost + A[x][y]
                    heappush(Q, (cost+A[x][y], x, y))
            return False

        l, r = 1, 10**9
        res = inf
        while r >= l:
            mid = (r + l) // 2
            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res