class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            res = []
            for i in range(n):
                temp = []
                for j in range(n):
                    temp.append(mat[j][i])
                res.append(temp[::-1])
            if res == target: return True
            mat = res
        return False