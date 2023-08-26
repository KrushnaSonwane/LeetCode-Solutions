class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        res, curr, i = [0] * n, 1, 0
        while candies >= curr:
            res[i%n] += curr
            candies -= curr
            curr += 1
            i += 1
        res[i%n] += candies
        return res