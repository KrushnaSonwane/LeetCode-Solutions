class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        t, pen = total, 0
        res = 0
        while t >= cost1:
            res += 1 + t // cost2
            t -= cost1
        res += t // cost2
        return res+1