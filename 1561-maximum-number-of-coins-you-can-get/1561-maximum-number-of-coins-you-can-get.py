class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res, i, taken = 0, len(piles)-2, len(piles) // 3
        piles.sort()
        while taken:
            res += piles[i]
            i -= 2
            taken -= 1
        return res