class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        res = s
        visit = set({s})
        Q = [s]
        while Q:
            currS = Q.pop()
            res = min(res, currS)
            A = []
            for ch in range(1, len(currS), 2):
                A.append(currS[ch - 1])
                A.append(str(((int(currS[ch]) + a) % 10)))
            A = ''.join(A)
            if A not in visit:
                Q.append(A)
                visit.add(A)
            A = currS[-b: len(currS)] + currS[:-b]
            if A not in visit:
                visit.add(A)
                Q.append(A)
        return res 