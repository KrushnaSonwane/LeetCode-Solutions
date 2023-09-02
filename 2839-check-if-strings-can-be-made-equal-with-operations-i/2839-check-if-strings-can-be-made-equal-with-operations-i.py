class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def solve(s1, s2):
            A, B = list(s1), list(s2)
            if A == B: return True
            A[0], A[2] = A[2], A[0]
            if A == B: 
                return True
            A[1], A[3] = A[3], A[1]
            if A == B: return True
            A[0], A[2] = A[2], A[0]
            if A == B: return True
            return False
        return solve(s1, s2) or solve(s2, s1)