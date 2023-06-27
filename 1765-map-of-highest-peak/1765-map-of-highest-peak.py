class Solution:
    def highestPeak(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        Q = [(i, j) for i in range(m) for j in range(n) if A[i][j]]
        visit = {(i, j) for i, j in Q}
        for i, j in Q: A[i][j] = 0
        res = 1
        while Q:
            for _ in range(len(Q)):
                i, j = Q.pop(0)
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if x in [-1, m] or y in [-1, n] or (x, y) in visit: continue
                    A[x][y] = res
                    visit.add((x, y))
                    Q.append((x, y))
            res += 1
        return A