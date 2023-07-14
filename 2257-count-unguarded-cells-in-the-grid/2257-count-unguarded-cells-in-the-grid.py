class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        w = {(i, j) for i, j in walls}
        rows, cols = set(), set()
        for i, j in guards:
            if (i, j) not in rows:
                for k in range(j, -1, -1):
                    if (i, k) in w: break
                    rows.add((i, k))
                for k in range(j, n):
                    if (i, k) in w: break
                    rows.add((i, k))
            if (i, j) not in cols:
                for k in range(i, -1, -1):
                    if (k, j) in w: break
                    cols.add((k, j))
                for k in range(i, m):
                    if (k, j) in w: break
                    cols.add((k, j))
        for c in cols:
            rows.add((c))
        return m*n - (len(rows)+len(w))