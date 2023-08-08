class Solution:
    def countServers(self, A: List[List[int]]) -> int:
        rows, cols = defaultdict(list), defaultdict(list)
        m, n = len(A), len(A[0])
        visit, res = set(), 0
        for r in range(m):
            for c in range(n):
                if A[r][c]:
                    rows[r].append((r, c))
                    cols[c].append((r, c))
        for r in range(m):
            for c in range(n):
                if A[r][c] and (r, c) not in visit:
                    visit.add((r, c))
                    count, Q = 0, [(r, c)]
                    while Q:
                        i, j = Q.pop(0)
                        count += 1
                        for x, y in rows[i]:
                            if (x, y) not in visit:
                                Q.append((x, y))
                                visit.add((x, y))
                        for x, y in cols[j]:
                            if (x, y) not in visit:
                                Q.append((x, y))
                                visit.add((x, y))
                    if count > 1: res += count
        return res