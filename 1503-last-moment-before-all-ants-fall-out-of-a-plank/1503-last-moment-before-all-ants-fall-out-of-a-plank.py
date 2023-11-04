class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0
        for l in left:
            res = max(res, l)
        for r in right:
            res = max(res, n - r)
        return res