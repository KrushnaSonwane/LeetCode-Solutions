class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[] for _ in matrix[0]]
        for li in matrix:
            for i in range(len(res)):
                res[i].append(li[i])
        return res