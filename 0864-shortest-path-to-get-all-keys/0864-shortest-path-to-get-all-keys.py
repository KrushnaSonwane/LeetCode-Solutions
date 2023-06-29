class Solution:
    def shortestPathAllKeys(self, A: List[str]) -> int:
        Q = []
        m, n = len(A), len(A[0])
        visit = set()
        count, res = 0, 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == '@': Q.append((i, j, ''))
                if A[i][j] in 'abcdef': count += 1
        visit.add((Q[0]))
        while Q:
            for _ in range(len(Q)):
                i, j, keys = Q.pop(0)
                if len(keys) == count: return res
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if x in [-1,m] or y in [-1,n] or A[x][y] == '#' or (x, y, keys) in visit: continue
                    if A[x][y] in 'ABCDEF' and A[x][y].lower() not in keys: continue
                    temp = keys
                    if A[x][y] in 'abcdef' and A[x][y] not in keys:
                        temp = keys + A[x][y]
                    visit.add((x, y, temp))
                    Q.append((x, y, temp))
            res += 1
        return -1