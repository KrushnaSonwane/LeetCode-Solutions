class Solution:
    def accountBalanceAfterPurchase(self, A: int) -> int:
        a, b = A, A
        while a % 10 != 0 and b %10 != 0:
            a += 1
            b -= 1
        if a % 10 == 0: return 100 -a
        return 100 - b