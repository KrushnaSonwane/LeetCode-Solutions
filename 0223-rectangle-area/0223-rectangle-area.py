class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        res = abs(ax2 - ax1) * abs(ay1 - ay2) + abs(bx2 - bx1) * abs(by1 - by2)
        x = min(ax2, bx2) - max(bx1, ax1)
        y = min(ay2, by2) - max(ay1, by1)
        if x > 0 and y > 0:
            res -= x * y
        return res