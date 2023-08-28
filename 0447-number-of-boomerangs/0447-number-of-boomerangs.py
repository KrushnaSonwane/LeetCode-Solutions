class Solution:
    def numberOfBoomerangs(self, A: List[List[int]]) -> int:
        res = 0
        for i in range(len(A)):
            hashT = defaultdict(int)
            for j in range(len(A)):
                f = A[i][0] - A[j][0]
                s = A[i][1] - A[j][1]
                hashT[f*f + s*s] += 1
            for num in hashT:
                res += hashT[num] * (hashT[num]-1)
        return res