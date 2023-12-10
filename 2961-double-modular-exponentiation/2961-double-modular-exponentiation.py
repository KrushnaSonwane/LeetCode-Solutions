class Solution:
    def getGoodIndices(self, A: List[List[int]], target: int) -> List[int]:
        '''((ai**bi % 10)**ci) % mi == target'''
        res = []
        for i, (a, b, c, m) in enumerate(A):
            sum_ = ((a**b) % 10) ** c
            if sum_ % m == target:
                res.append(i)
        return res