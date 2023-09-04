class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        A, B = [0 for _ in range(26)], [0 for _ in range(26)]
        for a, b in zip(s1, s2):
            A[ord(a)-97] += 1
            B[ord(b)-97] += 1

        def solve(A, B):
            a, b = 0, 0
            for x, y in zip(A, B):
                a, b = a + x, b + y
                if a > b: return False
            return True
        return solve(A, B) or solve(B, A)