class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        while start or goal:
            res += start%2 != goal%2
            start //= 2
            goal //= 2
        return res