class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        lastOne, lastZero = inf, 0
        count = 0
        for i, num in enumerate(nums):
            if num == 0:
                lastOne, lastZero = inf, i+1
                count = 0
            else:
                if num < 0:
                    count = (count+1) % 2
                if count == 1:
                    lastOne = min(lastOne, i+1)
                if count == 1:
                    res = max(res, i - lastOne + 1)
                else:
                    res = max(res, i - lastZero + 1)
        return res