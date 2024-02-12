class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n == 0 or n == 1 or n == 2: return min(n, 1)
        for _ in range(n-2):
            res = a + b + c
            a, b, c = b, c, res
        return res