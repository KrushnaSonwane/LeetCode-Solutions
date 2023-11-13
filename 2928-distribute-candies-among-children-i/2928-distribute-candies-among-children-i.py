class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(n, limit) + 1):
            for j in range(min(n, limit) + 1):
                for k in range(min(n, limit) + 1):
                    if i + j + k == n: res += 1
        return res