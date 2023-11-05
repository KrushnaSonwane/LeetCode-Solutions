class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        hashT = {i: 0 for i in range(n)}
        for a, b in edges:
            hashT[b] += 1
        count = 0
        res = -1
        for key in hashT:
            if hashT[key] == 0:
                count += 1
                res = key
        return -1 if count != 1 else res