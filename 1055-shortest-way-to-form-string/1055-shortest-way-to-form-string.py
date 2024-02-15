class Solution:
    def shortestWay(self, A: str, B: str) -> int:
        i, j = 0, 0
        res = 0
        while j < len(B):
            i, change = 0, 0
            while i < len(A) and j < len(B):
                if A[i] == B[j]:
                    j, change = j + 1, 1
                i += 1
            if not change: return -1
            res += 1
        return res