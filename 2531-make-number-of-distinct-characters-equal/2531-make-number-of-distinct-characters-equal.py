class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        AA, BB = collections.Counter(word1), collections.Counter(word2)
        m, n = len(AA), len(BB)
        if abs(m-n) > 2: return 0
        for a in AA:
            A, B = AA.copy(), BB.copy()
            A[a] -= 1
            if A[a]==0: del A[a]
            B[a] += 1
            for b in BB:
                A[b] += 1
                B[b] -= 1
                if B[b] == 0: del B[b]
                if len(A) == len(B): return 1
                A[b] -= 1
                if A[b] == 0: del A[b]
                B[b] += 1
        return 0