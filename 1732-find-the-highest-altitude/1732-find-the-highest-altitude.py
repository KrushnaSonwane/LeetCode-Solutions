class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = sum_ = 0
        for num in gain:
            sum_ += num
            res = max(res, sum_)
        return res