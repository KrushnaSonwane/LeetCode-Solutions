class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        a, b = 0, 0
        for num in range(1, n+1):
            a += num if num % m == 0 else 0
            b += num if num%m != 0 else 0
        return b - a