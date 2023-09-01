class Solution:
    def equalFrequency(self, word: str) -> bool:
        A = Counter(word)
        hashT = {A[ch] for ch in A}
        for ch in A:
            hashT = {A[ch]-1} if A[ch] > 1 else set()
            for ch2 in A:
                if ch != ch2:
                    hashT.add(A[ch2])
            if len(hashT) == 1: return True
        return False