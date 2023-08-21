class Solution:
    def getStrongest(self, A: List[int], k: int) -> List[int]:
        A.sort()
        res, m = [], A[(len(A)-1)//2]
        for a in A:
            res.append([abs(a-m), a])
        res.sort(key = lambda x: (-x[0], -x[1]))
        return [res[i][1] for i in range(k)]