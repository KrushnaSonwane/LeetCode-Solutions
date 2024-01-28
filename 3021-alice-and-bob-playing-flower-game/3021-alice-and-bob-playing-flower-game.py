class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        a, b, res = n // 2, m // 2, 0
        for i in range(1, n+1):
            if i % 2:
                res += b
            else:
                res = res + (m - b)
        return res