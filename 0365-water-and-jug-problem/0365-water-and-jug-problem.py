class Solution:
    def canMeasureWater(self, A: int, B: int, T: int) -> bool:
        if A%2==0 and B%2==0 and T%2: return 0
        if A+B < T: return 0
        visit, Q = set({(0,0)}), [(0,0)]
        while Q:
            a, b = Q.pop(0)
            if a + b == T: return True
            if a == 0:
                if (A, b) not in visit:
                    visit.add((A, b))
                    Q.append((A, b))
                if b != 0:
                    t = min(A, b)
                    b -= t
                    if (t, b) not in visit:
                        visit.add((t, b))
                        Q.append((t, b))
            else:
                if (0, b) not in visit:
                    visit.add((0,b))
                    Q.append((0, b))
                if b == 0:
                    if (a, B) not in visit:
                        visit.add((a, B))
                        Q.append((a, B))
                else:
                    t = min(a, B - b)
                    a -= t
                    b += t
                    if (a, b) not in visit:
                        visit.add((a, b))
                        Q.append((a, b))
            if b == 0:
                if (a, B) not in visit:
                    visit.add((a, B))
                    Q.append((a, B))
                if a != 0:
                    t = min(B, a)
                    a -= t
                    if (a, t) not in visit:
                        visit.add((a, t))
                        Q.append((a, t))
            else:
                if (a, 0) not in visit:
                    visit.add((a, 0))
                    Q.append((a, 0))
                if a == 0:
                    if (A, b) not in visit:
                        visit.add((A, b))
                        Q.append((A, b))
                else:
                    t = min(A-a, b)
                    a += t
                    b -= t
                    if (a, b) not in visit:
                        visit.add((a, b))
                        Q.append((a, b))
        return False