class Solution:
    def sortString(self, s: str) -> str:
        hashT = Counter(s)
        res, A = [], sorted([[ch, hashT[ch]] for ch in hashT])
        while len(res) != len(s):
            i = 0
            while len(A) > i:
                if A[i][1] > 0:
                    res.append(A[i][0])
                A[i][1] -= 1
                i += 1
            i -= 1
            while i > -1:
                if A[i][1] > 0:
                    res.append(A[i][0])
                A[i][1] -= 1
                i -= 1
        return ''.join(res)