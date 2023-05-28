class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: return 0
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        res = 0
        while fact and not fact % 10:
            res += 1
            fact //= 10
        return res