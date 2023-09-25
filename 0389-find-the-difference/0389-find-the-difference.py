class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        A, B = Counter(s), Counter(t)
        for ch in B:
            if B[ch] != A[ch]: return ch
        return '-1'