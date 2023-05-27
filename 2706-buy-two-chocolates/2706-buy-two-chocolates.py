class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        sum_ = prices[0] + prices[1]
        return money if sum_ > money else money - sum_