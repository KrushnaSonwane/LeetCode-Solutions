class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        A, B = sorted(s1[::2]), sorted(s2[::2])
        if A != B: return False
        A, B = sorted(s1[1::2]), sorted(s2[1::2])
        if A != B: return False
        return True