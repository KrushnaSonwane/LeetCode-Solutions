class Solution(object):
    def maxProfit(self, prices):
        res, min_ = 0, float("inf")
        for price in prices:
            min_ = min(price, min_)
            res = max(res, price - min_)
        return res
