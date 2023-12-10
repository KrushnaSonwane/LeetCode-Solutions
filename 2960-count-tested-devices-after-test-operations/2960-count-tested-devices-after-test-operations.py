class Solution:
    def countTestedDevices(self, A: List[int]) -> int:
        res = 0
        for i in range(len(A)):
            if A[i] > 0:
                res += 1
                for j in range(i+1, len(A)):
                    A[j] = max(0, A[j]-1)
        return res