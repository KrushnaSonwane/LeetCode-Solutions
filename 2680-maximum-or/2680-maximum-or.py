class Solution(object):
    def maximumOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        pre = []; suff = []
        sum_ = 0
        for num in nums:
            sum_ |= num
            pre.append(sum_)
        sum_ = 0
        for num in nums[::-1]:
            sum_ |= num
            suff.append(sum_)
        suff = suff[::-1] + [0]
        res = 0
        for i, num in enumerate(nums):
            currNum = num
            for _ in range(k):
                currNum *= 2
            if i > 0:
                res = max(res, pre[i - 1] | currNum | suff[i + 1])
            else:
                res = currNum | suff[i + 1]
        return res