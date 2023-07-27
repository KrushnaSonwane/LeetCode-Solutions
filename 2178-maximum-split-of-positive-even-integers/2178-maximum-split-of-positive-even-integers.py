class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2: return []
        res, curr, sum_ = [], 2, finalSum
        while sum_ >= curr:
            res.append(curr)
            sum_ -= curr
            curr += 2
        res[-1] += sum_
        return res