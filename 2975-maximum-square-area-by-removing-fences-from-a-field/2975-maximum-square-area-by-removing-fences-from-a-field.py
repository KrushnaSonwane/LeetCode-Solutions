class Solution:
    def maximizeSquareArea(self, m: int, n: int, A: List[int], B: List[int]) -> int:
        A.extend([1, m])
        B.extend([1, n])
        hashT, res, MOD = set(), -1, 10**9+7
        A.sort()
        B.sort()
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                hashT.add(A[j]-A[i])
        for i in range(len(B)):
            for j in range(i+1, len(B)):
                if B[j]-B[i] in hashT:
                    res = max(res, B[j]-B[i])
        return -1 if res == -1 else (res*res) % MOD