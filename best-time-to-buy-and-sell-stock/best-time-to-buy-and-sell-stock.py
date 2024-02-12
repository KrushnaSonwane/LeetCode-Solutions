class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, min_ = 0, float("inf")
        for price in prices:
            min_ = min(price, min_)
            res = max(res, price - min_)
        return res