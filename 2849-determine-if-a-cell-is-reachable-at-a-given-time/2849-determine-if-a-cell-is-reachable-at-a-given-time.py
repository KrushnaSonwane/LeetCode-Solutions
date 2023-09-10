class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        corners = min(abs(sx-fx), abs(sy-fy))
        dist = abs(sx-fx) + abs(sy-fy)
        if (sx, sy) == (fx, fy): 
            return t >= 2 or t == 0
        if corners > t: 
            return False
        if dist - corners*2 <= t-corners:
            return True
        return False