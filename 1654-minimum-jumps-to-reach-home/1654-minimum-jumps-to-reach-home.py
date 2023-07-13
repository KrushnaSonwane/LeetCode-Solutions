class Solution:
    def minimumJumps(self, F: List[int], a: int, b: int, x: int) -> int:
        visit, res = set(), 0
        max_ = max(x, max(F))+a+b
        for f in F:
            visit.add((f, 0))
            visit.add((f, 1))
        Q = [[0, 0]]
        while Q:
            for _ in range(len(Q)):
                pos, f = Q.pop(0)
                if pos == x: return res
                t = pos + a
                if max_ >= t and (t, 0) not in visit:
                    Q.append((t, 0))
                    visit.add((t, 0))
                t = pos-b
                if not f and t >= 1 and (t, 1) not in visit:
                    visit.add((t, 1))
                    Q.append((t, 1))
            res += 1
        return -1