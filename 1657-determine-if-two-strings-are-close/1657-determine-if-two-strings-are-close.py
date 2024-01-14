class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        A, B = Counter(word1), Counter(word2)
        for ch in A:
            if ch not in B:return False
        for ch in B:
            if ch not in A: return False
        A = sorted([A[a] for a in A])
        B = sorted([B[b] for b in B])
        return A == B