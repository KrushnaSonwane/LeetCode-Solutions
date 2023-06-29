class Solution:
    def minimumTime(self, A: List[List[int]]) -> int:
        D, Q = {}, [(0, 0, 0)] 
        if A[0][1] > A[0][0] + 1 and A[0][0] +1 < A[1][0]: return -1 
        m, n = len(A), len(A[0])
        while Q:
            time, i, j = heappop(Q)
            if (i, j) == (m-1, n-1): return time
            if (i, j) in D and D[(i, j)] <= time: continue
            D[(i, j)] = time
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if x in [-1,m] or y in [-1,n]: continue
                if A[x][y] > time:
                    dist = A[x][y] - time
                    if dist % 2 == 1:
                        heappush(Q, (dist + time, x, y))
                    else:
                        heappush(Q, (dist + time + 1, x, y))
                else:
                    heappush(Q, (time + 1, x, y))
        return -1