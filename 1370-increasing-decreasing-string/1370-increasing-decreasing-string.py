class Solution:
    def sortString(self, s: str) -> str:
        hashT = Counter(s)
        res, A = [], sorted([[ch, hashT[ch]] for ch in hashT])
        while len(res) != len(s):
            for i, (ch, count) in enumerate(A):
                if count > 0:
                    res.append(ch)
                A[i][1] -= 1
            A = A[::-1]
            for i, (ch, count) in enumerate(A):
                if count > 0:
                    res.append(ch)
                A[i][1] -= 1
            A = A[::-1]
        return ''.join(res)