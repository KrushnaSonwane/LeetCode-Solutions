class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        res, sum_, j = 0, 0, 0
        for i in range(1, target + 1):
            while j < len(coins) and coins[j] <= i:
                sum_ += coins[j]
                j += 1
            if sum_ >= i: continue    
            res, sum_ = res + 1, sum_ + i
        return res