class Solution(object):
    def longestString(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        res = 0
        if y > x:
            res += ((x * 2) * 2) + 2
            x = 0
            y -= x + 1
        elif y == x:
            res += (x * 2) * 2
            x = 0
            y = 0
        else:
            res += ((y * 2) * 2)+ 2
            x -= y
            y = 0
        if x:
            res = max(res, (res - 2) +( (2 * z) + 2))
        elif y:
            res += 2 * z
        else:
            res += 2 * z
        return res