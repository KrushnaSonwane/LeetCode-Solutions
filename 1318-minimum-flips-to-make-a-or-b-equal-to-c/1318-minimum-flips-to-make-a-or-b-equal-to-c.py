class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            x, y, z = a & 1, b & 1, c & 1
            a = a >> 1; b = b >> 1; c = c >> 1
            if x | y == z: continue
            res += x + y if not z else 1
        return res