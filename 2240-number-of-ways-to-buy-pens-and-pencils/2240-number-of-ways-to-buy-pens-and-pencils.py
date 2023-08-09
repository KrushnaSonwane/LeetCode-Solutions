class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res, t = 0, total
        while t >= cost1:
            res += 1 + t // cost2
            t -= cost1
        res += t // cost2
        return res+1