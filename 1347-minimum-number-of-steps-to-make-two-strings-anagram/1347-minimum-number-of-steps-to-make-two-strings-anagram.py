class Solution:
    def minSteps(self, s: str, t: str) -> int:
        A, B = Counter(s), Counter(t)
        res = 0
        for ch in B:
            res += max(0, B[ch]-A[ch])
        return res