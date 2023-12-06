class Solution:
    def totalMoney(self, n: int) -> int:
        A, res = [1, 2, 3, 4, 5, 6, 7], 0
        for i in range(n):
            res += A[i%7]
            A[i%7] += 1
        return res