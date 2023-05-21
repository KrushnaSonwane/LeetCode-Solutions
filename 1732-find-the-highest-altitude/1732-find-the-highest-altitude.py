class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res, sum_ = 0, 0
        for num in gain:
            sum_ += num
            res = max(res, sum_)
        return res