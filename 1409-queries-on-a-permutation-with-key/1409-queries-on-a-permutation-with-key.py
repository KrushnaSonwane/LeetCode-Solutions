class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        A = [i for i in range(1, m+1)]
        res = [0 for _ in queries]
        for i, Q in enumerate(queries):
            j = A.index(Q)
            res[i] = j
            newEle = A.pop(j)
            A = [newEle] + A
        return res