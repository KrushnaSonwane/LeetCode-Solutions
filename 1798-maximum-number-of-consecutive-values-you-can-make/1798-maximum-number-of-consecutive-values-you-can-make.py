class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        res, sum_ = 0, 0
        for num in coins:
            if num > sum_ + 1:
                break
            sum_ += num
            res = sum_
        return res + 1