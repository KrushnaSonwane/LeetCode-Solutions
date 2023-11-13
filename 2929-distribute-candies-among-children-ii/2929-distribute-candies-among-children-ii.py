class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(n, limit) + 1):
            j = min(limit, n - i)
            k = n - (i + j)
            if k <= limit:
                res += j - k + 1
        return res