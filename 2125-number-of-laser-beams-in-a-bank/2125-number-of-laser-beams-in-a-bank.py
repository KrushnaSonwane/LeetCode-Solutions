class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        A = []
        for b in bank:
            count = b.count('1')
            if count:
                A.append(count)
        res = 0
        for i in range(1, len(A)):
            res += A[i] * A[i-1]
        return res