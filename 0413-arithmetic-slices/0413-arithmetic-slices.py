class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res, count, lastNum, lastDiff = 0, 0, inf, inf
        for a in A:
            currDiff = lastNum - a
            if currDiff == lastDiff: count += 1
            else: count = 1
            lastDiff = currDiff
            lastNum = a
            if count > 1: res += count - 1
        return res