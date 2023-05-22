class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        beans.sort()
        suff, pre = sum(beans), 0
        res, n = float("inf"), len(beans)
        for i, num in enumerate(beans):
            suff -= num
            res = min(res, (suff - num * (n - i - 1)) + pre)
            pre += num
        return res