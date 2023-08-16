class Solution:
    def smallestSubsequence(self, S: str) -> str:
        hashT, A = Counter(S), []
        for ch in S:
            hashT[ch] -= 1
            if ch not in A:
                while A and A[-1] > ch and hashT[A[-1]] >= 1:
                    A.pop()
                A.append(ch)
        return ''.join(A)